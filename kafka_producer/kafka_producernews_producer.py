import requests
from kafka import KafkaProducer
import json
import time

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Your NewsAPI key
API_KEY = '3f991dc1a88240b18c272a7e41d07cf8'
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

def produce_news():
    while True:
        try:
            response = requests.get(url)
            news_json = response.json()

            if 'articles' in news_json:
                for article in news_json['articles']:
                    producer.send('news-topic', article)
                    print(f"[✔️ Sent] {article.get('title', 'No Title')}")
            else:
                print("[⚠️ Warning] No articles found or invalid API response.")

        except Exception as e:
            print(f"[❌ Error] {str(e)}")

        time.sleep(30)  # Wait 30 seconds before fetching again

if __name__ == "__main__":
    produce_news()
