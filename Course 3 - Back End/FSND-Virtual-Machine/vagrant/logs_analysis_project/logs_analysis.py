#!/usr/bin/env python
from flask import Flask, request, redirect, url_for

from logs_analysisdb import get_top_articles, get_top_authors, get_errored_days

app = Flask(__name__)

HTML_WRAP = '''\
    <!DOCTYPE html>
    <html>
        <head>
            <title>Logs Analysis</title>
            <style>
                h1, h2 { text-align: center; }
                textarea { width: 400px; height: 100px; }
                section { width: 34%%; margin: 0 33%% 0 33%%;
                 min-width: 350px; }
            </style>
        </head>
        <body>
            <h1>Logs Analysis</h1>
            <section class="top_articles">
                <h2>Top Articles</h2>
                <ol>
                %s
                </ol>
            </section>
            <section class="top_authors">
                <h2>Top Authors</h2>
                <ol>
                %s
                </ol>
            </section>
            <section class="error_list">
                <h2>Unusually Errored Days</h2>
                <ul>
                %s
                </ul>
            </section>
        </body>
    <html>
'''

VIEW_LIST_ITEM = '''\
    <li class="view_list_item">"%s" - %s Views</li>
'''

ERROR_LIST_ITEM = '''\
    <li class="error_item">%s - %s %% errors</li>
'''


@app.route('/', methods=['GET'])
def main():
    articles = "".join(VIEW_LIST_ITEM % (title, views) for title,
                       views in get_top_articles())
    authors = "".join(VIEW_LIST_ITEM % (name, views) for name,
                      views in get_top_authors())
    errors = "".join(ERROR_LIST_ITEM % (date, percent_errors) for date,
                     percent_errors in get_errored_days())
    html = HTML_WRAP % (articles, authors, errors)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
