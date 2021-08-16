import requests
import json
import re
  
# Opening JSON file
offline_dicitonary = {}
with open('./offline_dictionary/dictionary.json') as json_file:
    offline_dictionary = json.load(json_file)

def getWordMeaning(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    response = requests.get(url)
    try:
        return response.json()[0]['meanings']
    except:
        return []

def getOfflineWordMeaning(word):
    try:
        return offline_dictionary[word]
    except:
        return ''

def printOfflineDefinitions(definitions):
    definitions = re.split('\d+.', definitions)
    for index,definition in enumerate(definitions):
        if (index == 0 and definition == ''):
            continue
        elif (index == 0 and definition != ''):
            print(definition, '\n')
            continue
        else:
            print(index, definition[1:], '\n')
    


def listWordsMeaning(listOfWords):
    for word in listOfWords:
        offline_meaning = getOfflineWordMeaning(word)
        if(len(offline_meaning) != 0):
            print('Word: ',word, '\n')
            print('Definitions:', '\n')
            printOfflineDefinitions(offline_meaning)
            print('*' * 100, '\n')
            continue
        meanings = getWordMeaning(word)
        if(len(meanings) == 0):
            continue
        print('Word: ',word)
        for meaning in meanings:
            definitions = meaning['definitions']
            for index,definition in enumerate(definitions):
                print('Definition-' + str(index) + ': ', definition['definition'],'\n')
        print('*' * 100, '\n')

if __name__ == "__main__":
    listWordsMeaning(['atrocity', 'frugal', 'moderately'])
    #print(getOfflineWordMeaning('atroci'))