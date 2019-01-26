FROM python:3.7.2

LABEL maintainer="yuttasakcom@gmail.com"

WORKDIR /usr/src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 80

CMD [ "python", "/usr/src/server.py" ]
