FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir files

COPY . .

CMD [ "scrapy", "crawl", "user_api" ]