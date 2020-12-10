import logging
import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    numbers = requests.get("http://localhost:7071/api/Service2NumGen").text
    letters = requests.get("http://localhost:7071/api/Service3LetGen").text
    username = (''.join(numbers.text + letters.text) for i in range(5))
    
    return func.HttpResponse(f"Hello, {username}. This HTTP triggered function executed successfully.")
