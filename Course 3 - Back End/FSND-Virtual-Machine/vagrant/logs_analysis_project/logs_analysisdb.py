#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def get_top_articles():
    """Return the list of the top 3 articles in descending order by views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''select * from top_articles order by views desc limit 3''')
    articles = c.fetchall()
    db.close()
    return articles


def get_top_authors():
    """Return the list of the top 3 authors in descending order by views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''select authors.name, sum(top_articles.views) as author_views
     from top_articles, authors, articles
     where top_articles.title = articles.title and authors.id = articles.author
      group by authors.name order by author_views desc limit 3''')
    authors = c.fetchall()
    db.close()
    return authors


def get_errored_days():
    """Return the days where over 1% of the requests resulted in errors"""
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
