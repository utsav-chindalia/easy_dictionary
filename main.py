import io
from getText import detectText
from cleanText import cleanText
from listWordMeaning import listWordsMeaning

if __name__ == "__main__":
    response = detectText('./test_set/IMG_1539.JPG')
    with io.open('response.json', 'w') as response_file:
        response_file.write(response)
    words = cleanText(response)
    listWordsMeaning(words)
