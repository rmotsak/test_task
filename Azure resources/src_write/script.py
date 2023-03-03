import os
import time
from azure.storage.queue import QueueClient

# Retrieve the connection string for the storage account
connection_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]

# Create a client to access the queue
queue_client = QueueClient.from_connection_string(connection_string, "myqueue")

# Define the message to send
message = "Hello, Azure Storage Queue!"

# Send the message every minute
while True:
    queue_client.send_message(message)
    print(f"Message sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(60)
