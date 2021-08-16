import io
import json
def detectText(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    texts = response.text_annotations
    #print(texts[0].description)

    #for text in texts:
        #print('\n"{}"'.format(text.description))
        #dictionary.append(text.description)

        ## vertices = (['({},{})'.format(vertex.x, vertex.y)
                    ## for vertex in text.bounding_poly.vertices])

        ## print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    return texts[0].description



if __name__ == "__main__":
    response = detect_text('./test_set/IMG_1526.JPG')
    with io.open('response.json', 'w') as response_file:
        response_file.write(response)
    