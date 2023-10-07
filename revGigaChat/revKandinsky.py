import requests
import json
import time
import base64
import warnings
from PIL import Image
from io import BytesIO
def FB(prompt, width, height, negativ_prompt="", style=""):
    # URL, заголовки и данные для запроса
    url = "https://api.fusionbrain.ai/web/api/v1/text2image/run?model_id=1"
    headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryrlQE4GkVXTOCFaq3',
                'Origin': 'https://editor.fusionbrain.ai',
                'Pragma': 'no-cache',
                'Referer': 'https://editor.fusionbrain.ai/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
    }

    # Тело запроса
    data = f'------WebKitFormBoundaryrlQE4GkVXTOCFaq3\r\nContent-Disposition: form-data; name="params"; filename="blob"\r\nContent-Type: application/json\r\n\r\n{{"type":"GENERATE","style":"{style}","width":{width},"height":{height},"negativePromptDecoder":"{negativ_prompt}","generateParams":{{"query":"{prompt}"}}}}\r\n------WebKitFormBoundaryrlQE4GkVXTOCFaq3--\r\n'
    data=data.encode()
    # Отправляем POST-запрос
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 400 or response.status_code == 401 or response.status_code == 403:
        warnings.warn(str(json.loads(response.text)["message"]))
        return b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00\x00\x0cIDAT\x18Wc\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xa75\x81\x84\x00\x00\x00\x00IEND\xaeB`\x82'
    time.sleep(10)
    url = "	https://api.fusionbrain.ai/web/api/v1/text2image/status/"+json.loads(response.text)["uuid"]
    headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryrlQE4GkVXTOCFaq3',
                'Origin': 'https://editor.fusionbrain.ai',
                'Pragma': 'no-cache',
                'Referer': 'https://editor.fusionbrain.ai/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
    }

    # Отправляем POST-запрос
    response = requests.get(url, headers=headers)
    path='./out.png'
    # Выводим ответ сервера
    img = base64.b64decode(json.loads(response.text)["images"][0])
    return img
def get_style(style):
    style_slovar={"Аниме": "ANIME",
                  "Детальное фото": "UHD",
                  "Киберпанк": "CYBERPUNK",
                  "Кандинский": "KANDINSKY",
                  "Айвазовский": "AIVAZOVSKY",
                  "Малевич": "MALEVICH",
                  "Пикассо": "PICASSO",
                  "Гончарова": "GONCHAROVA",
                  "Классицизм": "CLASSICIS",
                  "Ренессанс": "RENAISSANCE",
                  "Картина маслом": "OILPAINTING",
                  "Рисунок карандашом": "PENCILDRAWING",
                  "Цифровая живопись": "DIGITALPAINTING",
                  "Средневековый стиль": "MEDIEVALPAINTING",
                  "Советский мультфильм": "SOVIETCARTOON",
                  "3D рендер": "RENDER",
                  "Мультфильм": "CARTOON",
                  "Студийное фото": "STUDIOPHOTO",
                  "Портретное фото": "PORTRAITPHOTO",
                  "Хохлома": "KHOKHLOMA",
                  "Новый год": "CRISTMAS"
                  }
    return style_slovar[style]
