import paho.mqtt.client as mqtt
import json

# MQTT Broker settings
broker = "mqtt.eclipse.org"
port = 1883
topic = "WaterMarkLevels"  # Define your topic

# Create a client instance
client = mqtt.Client()

# Define the callback for when a message is published
def on_publish(client, userdata, result):
    print("Data published successfully")

# Attach the callback function
client.on_publish = on_publish

# Connect to the broker
client.connect(broker, port, 60)

# Sample data to publish (could be dynamic)
data = {
    "Oroville/WML": [{"Date": "9/29/2024", "TAF": 2000}],
    "Shasta/WML": [{"Date": "9/29/2024", "TAF": 2720}],
    "Sonoma/WML": [{"Date": "9/29/2024", "TAF": 192}]
}

# Publish the data to the topic
client.loop_start()
client.publish(topic, json.dumps(data))  # Publishing JSON data
client.loop_stop()

print("Data has been published to the topic:", topic)
