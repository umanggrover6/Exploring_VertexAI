import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import HttpOptions, Part


load_dotenv()
location = os.getenv("GOOGLE_API_LOCATION")
project = os.getenv("GOOGLE_API_PROJECT")

client = genai.Client(vertexai=True,
                      project=project,
                      location=location,
                      http_options=HttpOptions(api_version="v1"))

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=["What is shown in the image?",
              Part.from_uri(file_uri="gs://cloud-samples-data/generative-ai/image/scones.jpg",
                            mime_type="image/jpeg",
                        ),
                    ],
)

print(response.text)