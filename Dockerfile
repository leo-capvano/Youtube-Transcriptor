FROM python:3.12

WORKDIR /yt-transcriptor

COPY requirements.txt ./requirements.txt
COPY ./app .
COPY ./.env ./.env
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "streamlit", "run", "./app.py" ]
