#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Prepare the SQL query with placeholders
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the state name as a parameter
    cursor.execute(sql_query, (state_name,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and search name from command-line arguments
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Connect to MySQL server
    c = db.cursor()

    # Execute the SQL query to retrieve all states
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

    # Fetch all rows and print the states
    [print(city) for city in c.fetchall()]
