FROM nikolaik/python-nodejs:python3.9.7-nodejs17
RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
COPY . /app/
WORKDIR /app/
RUN pip3 install -U pip
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
RUN pip3 install -U -r requirements.txt
CMD python3 -m Music
