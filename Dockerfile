FROM python:3.9

ADD . .

RUN pip install pyTelegramBotAPI python-dotenv loguru bs4


CMD [ "python", "./main.py" ]