import psycopg2

DBNAME = "news"


def get_top_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''select articles.title, count(log.path) as views from articles,
     log where log.path like '%' || articles.slug || '%'
     group by articles.title order by views desc''')
    articles = c.fetchall()
    db.close()
    return articles


def get_top_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''select authors.name, sum(top_articles.views) as author_views
     from top_articles, authors, articles
     where top_articles.title = articles.title and authors.id = articles.author
      group by authors.name order by author_views desc''')
    authors = c.fetchall()
    db.close()
    return authors


def get_errored_days():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''select total_errors.error_date as date,
    to_char((sum(total_errors.errors) / sum(total_requests.requests)) * 100,
     '0.9')  as percent_errors from (select log.time::timestamp::date as
      error_date, count(log.status) as errors from log where log.status
       not like '%200%' group by error_date) as total_errors,
        (select log.time::timestamp::date as request_date, count(log.status)
         as requests from log group by request_date) as total_requests
          where total_errors.error_date = total_requests.request_date
           group by date having (sum(total_errors.errors) /
            sum(total_requests.requests)) * 100 >= 1 order by date desc''')
    authors = c.fetchall()
    db.close()
    return authors
