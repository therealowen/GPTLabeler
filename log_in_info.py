# from cryptography.fernet import Fernet
# paid version API by OpenAI
from revChatGPT.V3 import Chatbot
class logInInfo:

    def __init__(self, keys):
        self.api_key = keys
    def connectAPI(self):
        chatbot = Chatbot(api_key= self.api_key)
        return chatbot
