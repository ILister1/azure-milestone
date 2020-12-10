import logging
import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    numbers = requests.get("https://usernamegenerator.azurewebsites.net/api/service2numgen").text
    letters = requests.get("https://usernamegenerator.azurewebsites.net/api/service3letgen").text
   # numbers = "86864"
   # letters = 'hyvmd'
    username = numbers + letters
    
    return func.HttpResponse(f"Hello, {username}. This HTTP triggered function executed successfully.")
