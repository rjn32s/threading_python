import paho.mqtt.client as mqtt
import threading

broker_url = "localhost" # replace with your broker URL
broker_port = 1883 # replace with your broker port

# Define your on_message callback function
def on_message(client, userdata, message):
    print("Received message on topic {}: {}".format(message.topic, message.payload))

# Create a Paho MQTT client object
client = mqtt.Client()

# Set the on_message callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker_url, broker_port)

# Define a list of topics to subscribe to
topics = ["topic1", "topic2", "topic3"]

# Define a function to handle each topic subscription
def subscribe_to_topic(topic):
    client.subscribe(topic)

# Create a list of threads to subscribe to each topic
threads = []
for topic in topics:
    thread = threading.Thread(target=subscribe_to_topic, args=(topic,))
    threads.append(thread)

# Start each thread
for thread in threads:
    thread.start()

# Loop to maintain the connection and receive messages
client.loop_forever()
