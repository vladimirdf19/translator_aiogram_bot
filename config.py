import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

X_RAPIDAPI_HOST = os.getenv('HOST_API')
X_RAPIDAPI_KEY = os.getenv('TRANSLATOR_API_KEY')

if __name__ == '__main__':
    print(TOKEN)
    print(X_RAPIDAPI_HOST)
    print(X_RAPIDAPI_KEY)
