import os
import time
from azure.storage.queue import QueueClient
from azure.core.exceptions import ResourceNotFoundError

# Retrieve the connection string for the storage account
connection_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
queue_name = "myqueue"

# Create a QueueClient object to interact with the queue
queue_client = QueueClient.from_connection_string(connection_string, queue_name)


# Load a message from the queue
while True:
    message = queue_client.receive_messages()
    if message:
        print("Received message:")
        print("Message ID:", message.id)
        print(f"Message: {message.content}")
        break
    else:
        print("No messages in the queue.")
        time.sleep(60)
