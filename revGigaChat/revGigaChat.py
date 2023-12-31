import requests
import json
import os
import uuid
import warnings
import asyncio, time
from telethon.sync import TelegramClient, events

class V1:
    def __init__(self, cookie, space_id, user_id, random_id=True, proxies = False):
        self.cookie = cookie
        if random_id:
            self.id = str(uuid.uuid4())
        else:
            self.id = random_id
        if proxies != False:
            self.proxies = {
               'http': 'http://'+proxies,
               'https': 'http://'+proxies,
            }
        else:
            self.proxies = False
        self.space_id = space_id
        self.user_id = user_id
    def GPT(self, message):
        headers_1={
				'Accept': 'text/event-stream',
                'Accept-Encoding': 'gzip, deflate, br',
				'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection': 'keep-alive',
				'Content-Type': 'application/json',
                'Cookie': self.cookie,
                'DNT': '1',
                'Origin': 'https://developers.sber.ru',
                'Pragma': 'no-cache',
                'Sec-Fetch-Dest': 'empty',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Site': 'same-origin',
				'TE': 'trailers',
				'space-id': self.space_id,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
				'X-KL-kfa-Ajax-Request': 'Ajax_Request',
                'user-id': self.user_id,
				
}
        headers_2={
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
                'TE': 'trailers',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',}
        if self.proxies == False:
            response = requests.post(
                'https://developers.sber.ru/api/chatwm/api/client/request_with_result_events?user-id='+self.user_id+"&space-id="+self.space_id,
                json={"mode":"request","request":{"request_json":message,"session_id":self.id,"model_type":"GigaChat:latest","preset":"default","generate_alternatives":"false","user_id":self.user_id}},
                headers=headers_1,
            )
            if response.status_code != 200:
                warnings.warn(str(json.loads(response.text)["message"]))
                return ""

            if response.status_code == 200:
                request_id = json.loads(response.text.split('\n')[2][6:])["request_id"]
                response = requests.get(
                    'https://developers.sber.ru/api/chatwm/api/client/get_result_events?request_id='+str(request_id)+'&space-id=' + self.space_id + '&user-id=' + self.user_id,
                    headers=headers_2)
        if self.proxies != False:
            response = requests.post(
                'https://developers.sber.ru/api/chatwm/api/client/request_with_result_events?user-id='+self.user_id+"&space-id="+self.space_id,
                json={"mode":"request","request":{"request_json":message,"session_id":self.id,"model_type":"GigaChat:latest","preset":"default","generate_alternatives":"false","user_id":self.user_id}},
                headers=headers_1,
                proxies=self.proxies
            )
            if response.status_code != 200:
                warnings.warn(str(json.loads(response.text)["message"]))
                return ""

            if response.status_code == 200:
                request_id = json.loads(response.text.split('\n')[2][6:])["request_id"]
                response = requests.get(
                    'https://developers.sber.ru/api/chatwm/api/client/get_result_events?request_id='+str(request_id)+'&space-id=' + self.space_id + '&user-id=' + self.user_id,
                    headers=headers_2,
                    proxies=self.proxies)
                        
        q = response.content.decode('UTF-8').split("\n")
        q = json.loads(q[len(q)-3].replace("data: ", ""))
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
