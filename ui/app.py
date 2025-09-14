import streamlit as st
import psycopg2
import time
import logging
from psycopg2 import OperationalError

logging.basicConfig(level=logging.INFO)

DB_HOST = "postgres"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_PORT = "5432"

def fetch_data():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute("SELECT * from sentences;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except OperationalError as e:
        st.error(f"Error connecting to the database: {e}")
        return []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []
def main():
    st.title("Real-time Sentiment Analysis Dashboard")
    st.markdown("This dashboard displays sentences and their sentiment scores from the PostgreSQL database.")
    unique_id = set()
    while True:
        data = fetch_data()
        if data:
            for row in data:
                id=row[0]
                if id in unique_id:
                    continue
                st.write(row)
                unique_id.add(id)
        else:
            st.write("No data available or unable to connect to the database.")
        
        time.sleep(5) 

if __name__ == "__main__":
    main()