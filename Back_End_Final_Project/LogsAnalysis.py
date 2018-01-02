#!/usr/bin/python
import psycopg2

'''
1. What are the most popular three articles of all time? Which articles have
been accessed the most? Present this information as a sorted list with the
most popular article at the top.
'''
query_one_question = 'What are the most popular three articles of all time?'
# Store the query question
query_one = (
    "SELECT title, count(*) from log l "
    "left join articles a "
    "on substring (l.path, 10, length(a.slug)) = a.slug "
    "where path like '%/article/%' group by title "
    "order by count desc limit 3")

'''
2. Who are the most popular article authors of all time? That is, when you sum
up all of the articles each author has written, which authors get the most page
views? Present this as a sorted list with the most popular author at the top.
'''
query_two_question = 'Who are the most popular article authors of all time?'
query_two = (
    "SELECT name, SUM(count) from "
    "(SELECT slug, count(*), name from "
    "(SELECT paSlug.path, paSlug.slug, aut.name from "
    "(SELECT lo.path, art.slug, art.author from log lo "
    "left join articles art "
    "on substring (lo.path, 10, length(art.slug)) = art.slug "
    "where path like '%/article/%') paSlug "
    "left join authors aut on paSlug.author = aut.id) artNamed "
    "group by slug, name) artCount group by name order by sum desc")

'''
3. On which days did more than 1% of requests lead to errors? The log table
includes a column status that indicates the HTTP status code that the news
site sent to the user's browser. (Refer to this lesson for more information
about the idea of HTTP status codes.)
'''
query_three_question = 'On which days did more than 1% of requests '\
    'lead to errors?'
query_three = (
    "SELECT d.date, round(errorCount.count/sum.sum*100,2) as percent "
    "from (SELECT distinct substring(cast(time as text), 1, 10) as date "
    "from log) d left join (SELECT date, sum(count) from "
    "(SELECT date, status, count(*) from "
    "(SELECT status, substring(cast(time as text), 1, 10) as date from log) a "
    "group by date, status) b group by date) sum on d.date = sum.date "
    "left join (SELECT substring(cast(log.time as text), 1, 10) as date, "
    "count(*) as count from log where status = '404 NOT FOUND' "
    "group by date) errorCount on d.date = errorCount.date "
    "where (errorCount.count/sum.sum*100) > 1")


def connect():
    # Connect to the PostgreSQL server
    try:
        # Connect to an existing database
        conn = psycopg2.connect("dbname=news")
        # Create a cursor to eprorm database operations
        cursor = conn.cursor()
        return cursor, conn
    # Return an error message of unable to connect
    except:
        print ("Unable to connect to database.")


def execute_query(query, cur):
    # Execute query
    cur.execute(query)
    # Returns all query results
    results = cur.fetchall()
    return results


def print_query_results(results):
    # Print count query results
    print '\n' + results[0] + '\n'
    num = 1
    for row in results[1]:
        print str(num) + '. : ' + str(row[0]) + '\t ' + str(row[1]), results[2]
        num += 1

# Get the database connection and the cursor
cur, conn = connect()

# Execute and store query question and results
query_one_results = query_one_question, execute_query(query_one, cur), ' hits'
query_two_results = query_two_question, execute_query(query_two, cur), ' hits'
query_three_results = query_three_question, execute_query(
    query_three, cur), '% errors'

# Print query results
print_query_results(query_one_results)
print_query_results(query_two_results)
print_query_results(query_three_results)


# Close the database connection
conn.close()
