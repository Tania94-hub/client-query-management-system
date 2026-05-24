import pandas as pd
from db_config import connection, cursor

# Read CSV file
df = pd.read_csv("synthetic_client_queries (1).csv")

# Show first 5 rows
print(df.head())

# -------------------------------
# DELETE OLD DATA TO PREVENT DUPLICATES
# -------------------------------

cursor.execute("DELETE FROM queries")
connection.commit()

# -------------------------------
# INSERT DATA INTO MYSQL
# -------------------------------

for _, row in df.iterrows():

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
        row['query_id'],
        row['client_email'],
        str(row['client_mobile']),
        row['query_heading'],
        row['query_description'],
        row['status'],
        row['date_raised'],
        None if pd.isna(row['date_closed']) else row['date_closed']
    )

    cursor.execute(query, values)

# Save all inserted rows
connection.commit()

print("Dataset Imported Successfully")