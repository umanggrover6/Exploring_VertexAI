import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import HttpOptions, ModelContent, Part, UserContent

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

chat = client.chats.create(
    model="gemini-2.0-flash-001",
    history=[
        UserContent(parts=[Part(text="Hello")]),
        ModelContent(
            parts=[Part(text="Great to meet you. What would you like to know?")],
        ),
    ],
)
response = chat.send_message("What are all the colors in a rainbow?")
print(response.text)

