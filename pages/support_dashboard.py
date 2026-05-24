import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

from query_operations import (
    fetch_queries,
    fetch_queries_by_status,
    close_query
)

st.title("Support Team Dashboard")

# Filter option
filter_option = st.selectbox(
    "Filter Queries",
    ["All", "Open", "Closed"]
)

# Fetch data
if filter_option == "All":
    data = fetch_queries()

else:
    data = fetch_queries_by_status(filter_option)

# Convert to DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Query ID",
        "Mail ID",
        "Mobile Number",
        "Query Heading",
        "Query Description",
        "Status",
        "Created Time",
        "Closed Time"
    ]
)

st.dataframe(df)

# ---------------- ANALYTICS ---------------- #

st.subheader("Query Analytics")

total_queries = len(df)

open_queries = len(df[df["Status"] == "Open"])

closed_queries = len(df[df["Status"] == "Closed"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Queries", total_queries)

col2.metric("Open Queries", open_queries)

col3.metric("Closed Queries", closed_queries)

# Pie Chart

labels = ["Open", "Closed"]

sizes = [open_queries, closed_queries]

# Prevent pie chart crash when values are zero
if sum(sizes) > 0:

    fig, ax = plt.subplots()

    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%'
    )

    ax.axis('equal')

    st.pyplot(fig)

else:
    st.warning("No query data available for analytics.")

st.subheader("Close Query")

query_id = st.text_input("Enter Query ID")

if st.button("Close Query"):

    close_query(query_id)

    st.success("Query Closed Successfully")