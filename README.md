# Real-time-sentiment-analysis
Real-time data pipeline using Kafka, Redis, PostgreSQL, and Streamlit. Producer streams text data, Consumer performs sentiment analysis and stores it in Postgres and temporarily in redis cache.  Streamlit visualizes the data live. Fully containerized with Docker Compose for easy deployment and scaling.

Open a terminal and go to the project root directory.

Start the docker engine and run "docker compose up -d" .

Open localhost:8501 in your browser and you will see the real time sentiments coming from producer.
