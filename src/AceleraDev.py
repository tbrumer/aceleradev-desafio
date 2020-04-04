import Constants
from src.Util import Util


class aceleraDev:

    def __init__(self):
        self.util = Util()
        self.apiRequestUrl = Constants.API_REQUEST_URL
        self.apiResponseUrl = Constants.API_RESPONSE_URL
        self.apiToken = Constants.TOKEN

    def start(self):
        response = self.util.getResponse(self.apiRequestUrl, self.apiToken)
        self.util.saveToFile(Constants.ANSWER_FILE, response)

    def end(self):
        response = self.util.sendResponse(self.apiResponseUrl, self.apiToken, Constants.ANSWER_FILE)
        print(response.json())

    def decrypt(self):
        pList = []
        decryptedText = ''

        data = self.util.readJson(Constants.ANSWER_FILE)
        print('Encrypted: ' + data[Constants.ENCRYPTED])
        decryptingNumber = data[Constants.NUMBER]
        for p in data[Constants.ENCRYPTED]:
            pList.append(p)

        for x in range(0, len(pList)):
            if pList[x] in Constants.ALPHABET:
                pPosition = Constants.ALPHABET.find(pList[x])
                if not pPosition - decryptingNumber < 0:
                    pDecrypted = (Constants.ALPHABET[pPosition - decryptingNumber])
                    pList[x] = pDecrypted
                else:
                    difference = abs(pPosition - decryptingNumber)
                    pList[x] = Constants.ALPHABET[len(Constants.ALPHABET) - difference]

        for p in pList:
            decryptedText += p

        self.util.refreshFile(Constants.ANSWER_FILE, Constants.DECRYPTED, decryptedText)

        print('Decrypted: ' + decryptedText)

    def generateHash(self):
        data = self.util.readJson(Constants.ANSWER_FILE)
        hash = self.util.generateSha1(data[Constants.DECRYPTED])
        self.util.refreshFile(Constants.ANSWER_FILE, Constants.CRYPTOGRAPHY_RESUME, hash)
