import requests
import json
import os
import uuid
import warnings
import asyncio, time
from telethon.sync import TelegramClient, events

class V1:
    def __init__(self, cookie, space_id, user_id, random_id=True):
        self.cookie = cookie
        if random_id:
            self.id = str(uuid.uuid4())
        else:
            self.id = random_id
        self.space_id = space_id
        self.user_id = user_id
    def GPT(self, message):
        response = requests.post(
			'https://developers.sber.ru/api/chatwm/api/client/request',
			json={"generate_alternatives":"false","request_json":message,"session_id":self.id,"model_type":"GigaChat:v1.3.0","preset":"default"},
			headers={
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
				'Accept': 'application/json, text/plain, */*',
				'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
				'Accept-Encoding': 'gzip, deflate, br',
				'Content-Type': 'application/json',
				'user-id': self.user_id,
				'space-id': self.space_id,
				'X-KL-kfa-Ajax-Request': 'Ajax_Request',
				'Origin': 'https://developers.sber.ru',
				'DNT': '1',
				'Connection': 'keep-alive',
				'Cookie': self.cookie,
				'Sec-Fetch-Dest': 'empty',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Site': 'same-origin',
				'TE': 'trailers'
					 },
		)
        if response.status_code == 401 or response.status_code == 403:
            warnings.warn(eval(response.text)["message"])
            return ""
        if response.status_code == 200:
            request_id = eval(response.text)["request_id"]
            response = requests.get(
                            'https://developers.sber.ru/api/chatwm/api/client/get_result_events?request_id='+str(request_id)+'&space-id=' + self.space_id + '&user-id=' + self.user_id,
                            headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
                                    'Accept': 'text/event-stream',
                                    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                                    'Accept-Encoding': 'gzip, deflate, br',
                                    'DNT': '1',
                                    'Connection': 'keep-alive',
                                    'Cookie': self.cookie,
                                    'Sec-Fetch-Dest': 'empty',
                                    'Sec-Fetch-Mode': 'cors',
                                    'Sec-Fetch-Site': 'same-origin',
                                    'Pragma': 'no-cache',
                                    'Cache-Control': 'no-cache',
                                    'TE': 'trailers'
                                             },
                    )
            q = response.content.decode('UTF-8').split("\n")
            q = eval(q[len(q)-3].replace("data: ", ""))
            q = q["responses"][0]['data']
            q = q.replace('<image src="', '<image src="https://developers.sber.ru/studio/generated-images/')
            return q

class V2:
    def __init__(self, api_id, api_hash):
        
        self.api_id = api_id
        self.api_hash = api_hash

        self.client = TelegramClient('session_name', api_id, api_hash, system_version="4.16.30-vxHOME-PC")

    async def send_telegram_message(self, message, time_sleep = 5, new_chat = False):
        async with self.client:

            recipient = '@gigachat_bot'

            if new_chat:
                sent_message = await self.client.send_message(recipient, "/restart")
            sent_message = await self.client.send_message(recipient, message)
            time.sleep(time_sleep)
            
            response_messages = []
            async for event in self.client.iter_messages(recipient, limit=1):
                response_messages.append(event.text)
                if len(response_messages) == 1:
                    break

            return response_messages[0]
