from google.cloud import vision
import io
import requests



# """Extrai texto de uma imagem usando Google Vision API."""

def extract_text_from_image(image_path):

    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)

    texts = response.text_annotations
    if texts:
        return texts[0].description  # Retorna o texto principal detectado

    return None






