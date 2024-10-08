import json
import time
import base64
import requests

from config import KandinskyConfig


class Text2ImageAPI:
    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS, timeout=300)
        data = response.json()
        print(data)
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }
        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data,
                                 timeout=300)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS,
                                    timeout=300)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']
            attempts -= 1
            time.sleep(delay)


def generate_image(prom):
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/',  str(KandinskyConfig.KANDINSKY_API_KEY),
                        str(KandinskyConfig.KANDINSKY_SECRET_KEY))
    model_id = api.get_model()
    uuid = api.generate(prom, model_id)
    images = api.check_generation(uuid)
    image_base64 = images[0]
    image_data = base64.b64decode(image_base64)
    try:
        with open("assets/temporary/generated.jpg", "wb") as file:
            file.write(image_data)
    except Exception as e:
        print(e)
        with open("assets/temporary/generated.jpg", "w+") as file:
            file.write(image_data)


def request_image(req):
    generate_image(req.replace("\n", " "))
    print("завершено")
