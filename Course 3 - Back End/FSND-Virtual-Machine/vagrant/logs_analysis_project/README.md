# My Logs Analysis Project

A python web application that performs analyses on news article view data and
error logs. To do this it uses a mock PostgreSQL database in python script to
answer the following 3 questions:
* What are the top 3 most viewed articles?
* What are the top 3 most viewed authors?
* What days did the error codes reach over 1% of the total daily requests for
  the webpage?

## Requirements

* Python 2.7.12
* Flask 0.12.2
* VirtualBox 5.1.32
* Vagrant 2.0.2
* FSND Virtual Machine configuration files. [Repository](https://github.com/udacity/fullstack-nanodegree-vm "Download VM configuration files")
* The creation of the top_articles view

## How to run the app

Open the command prompt in the downloaded FSND Virtual Machine folder. In it
type: `vagrant up` press enter, and then enter `vagrant ssh` and press enter.

Ensure that the logs_analysis_project folder is moved into the vagrant folder
in the FSND Virtual Machine directory.

  `cd` into the logs_analysis_project directory and in the command prompt
enter `psql -d news -f newsdata.sql` to load the data into the local database.

To run the program you will need to make sure you meet the listed requirements,
and create the top_articles view.

To create the top articles view in the command prompt you must enter
`psql news` to enter the psql command prompt for the news database. If
you entered it correctly your command prompt will display `news=>`.

In the psql command prompt in order to create the top_articles view enter t
following:
```sql
create view top_articles as select articles.title, count(log.path) as views
from articles, log where log.path = '/article/' || articles.slug group by
articles.title order by views desc;
```

Enter `\q` in the command prompt to quit the database prompt.

Ensure that you are in the logs_analysis_project directory, and in the command
prompt enter `python logs_analysis.py`. This will initialize the application.

To view the application you must open your browser and enter `localhost:8000`
in the address bar.

Authored by: Adam Gallant, 2018-01-05
