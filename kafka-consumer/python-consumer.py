from kafka import KafkaConsumer
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import psycopg2

nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='postgres',
    host='postgres',
    port='5432'
)
cur = conn.cursor()

kafka_nodes = "kafka:9092"
myTopic = "sentence"

consumer = KafkaConsumer(
    myTopic,
    bootstrap_servers=kafka_nodes,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    print(data)
    scores = analyzer.polarity_scores(data['sentence'])
    print(scores['compound'])
    cur.execute(
        "INSERT INTO sentences (sentence, sentiment) VALUES (%s, %s)",
        (data['sentence'], scores['compound'])
    )
    conn.commit()