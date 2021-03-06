FROM python:3.8-buster

RUN apt-get update && apt-get install -y sox normalize-audio

RUN mkdir djangoAdmin
WORKDIR djangoAdmin
COPY requirements.txt .
RUN pip install -r ./requirements.txt
RUN pip install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/archive/master.zip
COPY . .

RUN cat ./SuiSiannAdmin/docker_tsuki.py >> ./SuiSiannAdmin/settings.py

EXPOSE 8000
CMD gunicorn SuiSiannAdmin.wsgi \
  -b 0.0.0.0:8000 \
  --log-level debug

