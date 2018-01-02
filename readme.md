# Udacity IPND Final Project

## About This Program
    This is the final project in the Intro to Programming Nanodegree. In this project, we will practice interacting with a live database both from the command line and from our code. We will explore a large database with over a million rows. Finally, we will build and refine complex queries and use them to draw business conclusions from data.


## Setup Requirements
    This project makes use of the same Linux-based virtual machine (VM). To run the progream, you will need:
    - Python2
    - Vagrant
    - VirtualBox

    You will also need to download the data from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip/. You will need to unzip the file and move `newsdata.sql` to the `vagrant` directory, which is shared with your virtual machine.

## How to Run
    To execute the program, run python3 newsdata.py from the command line.

    To run the virtual machine you will need to enter the command `vagrant up` followed by `vagrant ssh`.

    To connect to the database and load the data, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`.


## Expected Output

What are the most popular three articles of all time?

1. : Candidate is jerk, alleges rival    342102  hits
2. : Bears love berries, alleges bear    256365  hits
3. : Bad things gone, say good people    171762  hits

Who are the most popular article authors of all time?

1. : Ursula La Multa     512805  hits
2. : Rudolf von Treppenwitz      427781  hits
3. : Anonymous Contributor       171762  hits
4. : Markoff Chaney      85387  hits

On which days did more than 1% of requests lead to errors?

1. : 2016-07-17  2.26 % errors