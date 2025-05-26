import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import vertexai.preview.vision_models

def generate_image(
        project_id: str,
        location: str,
        output_file: str,
        prompt: str
) -> vertexai.preview.vision_models.ImageGenerationResponse:
    """Generates an image based on the provided text prompt.
    Args:
        project_id (str): Google Cloud project ID.
        location (str): Location for the Vertex AI service.
        output_file (str): Path to save the generated image.
        prompt (str): Text prompt to generate the image."""
    
    # Initialize the Vertex AI client
    vertexai.init(project=project_id, location=location)

    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")

    image = model.generate_images(prompt=prompt,
                                    number_of_images=1,
                                    seed=42,
                                    add_watermark=False)
    
    # Save the generated image to a file
    image[0].save(output_file)  
        
    return image


import os
from dotenv import load_dotenv
load_dotenv()

# Load environment variables
project_id = os.getenv("GOOGLE_API_PROJECT")    
location = os.getenv("GOOGLE_API_LOCATION")

generate_image(
    project_id=project_id,
    location=location,
    output_file='image.jpeg',
    prompt='Create an image of a person holding a cricket bat signed by Indian Cricketer Virat Kohli.',
    )
