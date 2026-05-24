from datetime import datetime
from db_config import connection, cursor


# Insert new query
def insert_query(
    query_id,
    mail_id,
    mobile_number,
    query_heading,
    query_description
):

    query = """
    INSERT INTO queries (
        query_id,
        mail_id,
        mobile_number,
        query_heading,
        query_description,
        status,
        query_created_time,
        query_closed_time
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        query_id,
        mail_id,
        mobile_number,
        query_heading,
        query_description,
        "Open",
        datetime.now(),
        None
    )

    cursor.execute(query, values)

    connection.commit()

    # Fetch all queries
def fetch_queries():

    query = "SELECT * FROM queries"

    cursor.execute(query)

    return cursor.fetchall()


# Fetch queries by status
def fetch_queries_by_status(status):

    query = """
    SELECT * FROM queries
    WHERE status = %s
    """

    cursor.execute(query, (status,))

    return cursor.fetchall()


# Close query
def close_query(query_id):

    query = """
    UPDATE queries
    SET status = %s,
        query_closed_time = %s
    WHERE query_id = %s
    """

    values = (
        "Closed",
        datetime.now(),
        query_id
    )

    cursor.execute(query, values)

    connection.commit()