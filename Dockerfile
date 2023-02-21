FROM python:3.10

WORKDIR /mediabot

COPY . .

RUN pip install pyTelegramBotAPI python-dotenv loguru bs4 cloudscraper


CMD [ "python", "main.py" ]


# run magraitions.py
# docker build . -t mediabot
# docker run -v $(pwd):/mediabot mediabot