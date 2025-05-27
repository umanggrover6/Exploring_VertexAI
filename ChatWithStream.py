import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import HttpOptions

import logging
from google.cloud import logging as gcp_logging

# ------  Below cloud logging code is for Qwiklab's internal use, do not edit/remove it. --------
# Initialize GCP logging
gcp_logging_client = gcp_logging.Client()
gcp_logging_client.setup_logging()

load_dotenv()
location = os.getenv("GOOGLE_API_LOCATION")
project = os.getenv("GOOGLE_API_PROJECT")

client = genai.Client(vertexai=True,
                      project=project,
                      location=location,
                      http_options=HttpOptions(api_version="v1"))

chat = client.chats.create(model="gemini-2.0-flash-001")
response_text = ""

for chunk in chat.send_message_stream("What are all the colors in a rainbow?"):
    print(chunk.text, end="")
    response_text += chunk.text

