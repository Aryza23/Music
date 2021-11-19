FROM nikolaik/python-nodejs:python3.10-nodejs17
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN pip3 install -U pip
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
RUN pip3 install -U -r requirements.txt
CMD python3 -m Music
