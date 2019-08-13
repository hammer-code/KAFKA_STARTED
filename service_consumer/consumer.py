
from kafka import KafkaConsumer
from dotenv import load_dotenv
import logging
import json
import os
import smtplib
import ssl


load_dotenv()
MAIL_USERNAME=os.getenv("MAIL_USERNAME")
MAIL_PASSWORD=os.getenv("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER=os.getenv("MAIL_DEFAULT_SENDER")

def get_kafka_consumer(broker, topic):
    try:
        consumer = KafkaConsumer(
                topic,
                bootstrap_servers=[broker],
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    except Exception as e:
        print(e)
        exit()
    else:
        return consumer

def send_email(email, subject, message):
    context = ssl.create_default_context()
    smtp_server = "smtp.gmail.com"
    port = 587
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  
        server.starttls(context=context)
        server.ehlo()  
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.sendmail(MAIL_DEFAULT_SENDER, email, message)
    

broker = "localhost:9092"
topic = "email_service"
data = list()
consumer = get_kafka_consumer(broker, topic) 
for message in consumer:
    data = message.value
    email = data['email']
    subject = data['subject']
    value = data['messages']
    print("Email : ", email)
    print("Subject : ", subject)
    print("Message : ", value)
    send_email(email, subject, value)
    print("Mail Send")

    
