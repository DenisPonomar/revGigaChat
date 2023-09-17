# revGigaChat
# Описание
Реверс-инжиниринг GigaChat от СберБанк России
# Отказ от отственноости
Используя этот репозиторий или любой связанный с ним код, вы соглашаетесь с [официальным уведомлением](https://github.com/DenisPonomar/revGigaChat/blob/main/LEGAL_NOTICE.md). Автор не несет ответственности за любые копии, форки, повторные загрузки, сделанные другими пользователями, или что-либо еще, связанное с revGigaChat. Это единственный аккаунт и репозиторий автора. Чтобы предотвратить выдачу себя за другое лицо или безответственные действия, соблюдайте лицензию GNU GPL, которую использует этот репозиторий. 
# Установка
```
pip install -U git+https://github.com/DenisPonomar/revGigaChat.git
```
# Использование
## Через developers.sber.ru/studio/workspaces
### Подготовка
* Перейдите по ссылке https://developers.sber.ru/studio/workspaces/
* Авторизуйтесь
* На странице личного пространства нажмите "Все инструменты", далее выберите "Модель GigaChat" и создайте проект
* Откройте проект
* Откройте инструменты разработчика через F12
* Перейдите во вкладку "Сеть" или "Network
* Отправьте сообщение GigaChat
* Найдите запрос на https://developers.sber.ru/api/chatwm/api/client/
* Из заголовков запроса скопируйте значения Cookie, space-id и user-id
### Создание нового чата
```
from revGigaChat import revGigaChat
Chat = revGigaChat.V1(cookie = "Cookie", space_id = "space-id", user_id = "user-id")
print(Chat.GPT("Привет"))
```
### Использование чата с заданным id
id представляет из себя строку uuid
```
from revGigaChat import revGigaChat
Chat = revGigaChat.V1(cookie = "Cookie", space_id = "space-id", user_id = "user-id", random_id="id")
print(Chat.GPT("Привет"))
```
### Плюсы
* Возможность параллельно работать с несколькими чатами
### Минусы
* Необходимо иметь российский IP
* Каждые несколько дней нужно получать новый Cookie
## Через клиент Telegram
* Перейдите по ссылке https://my.telegram.org/auth
* Откройте "API development tools"
* Скопируйте "App api_id" и "App api_hash"
```
from revGigaChat import revGigaChat
import asyncio
Chat = revGigaChat.V2(api_id='api_id', api_hash='api_hash')
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Chat.send_telegram_message(message = "Привет", time_sleep = 5, new_chat = False)))
```
После первого запуска последовательно введите номер телефона и код безопасности. Рядом с вашим скриптом создастся файл session_name.session - не удаляйте его.
### Необязательные параметры
* time_sleep устанавливает задержу по времени между отправкой сообщения боту @gigachat_bot и анализом последних сообщений в чате. По умолчанию 5 секунд. При слишком маленькой задержке по времени есть риск получить в ответ "Классный запрос, @exmaplename! 💭Прочитал, думаю над ответом".
* new_chat устанавливает отправлять боту @gigachat_bot сообщение "/restart" (при значении True) или нет (при значении False). По умолчанию False.
### Плюсы
* Нет необходимости иметь российский IP
### Минусы
* Работа только с одним чатом
