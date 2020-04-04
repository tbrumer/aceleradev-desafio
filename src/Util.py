import requests
import json
import hashlib


class Util:

    def getResponse(self, url, token):
        return requests.get(url + token)

    def sendResponse(self, url, token, file):
        return requests.post(url + token, files={'answer': open(file, 'rb')})

    def saveToFile(self, fileName, response):
        with open(fileName, 'w') as outfile:
            json.dump(response.json(), outfile, indent=2)

    def readJson(self, fileName):
        with open(fileName) as json_file:
            data = json.load(json_file)
        return data

    def refreshFile(self, fileName, key, value):
        with open(fileName, 'r+') as json_file:
            data = json.load(json_file)
            data[key] = value
            json_file.seek(0)
            json.dump(data, json_file, indent=2)
            json_file.truncate()

    def generateSha1(self, text):
        return hashlib.sha1(text).hexdigest()
