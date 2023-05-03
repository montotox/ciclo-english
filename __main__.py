import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk_errors import SlackApiError

# Load the token from .env file
load_dotenv()

# Create a slack client
client = WebClient(token=os.environ.get("SLACK_TOKEN"))

try:
    response = client.chat_postMessage(
        channel="#testing-bot",
        text="Recuerda que hoy es día de escribir en inglés"
    )
    print("Message sent successfully", response["ts"])
except SlackApiError as e:
    print("Error creating conversation: {}".format(e))