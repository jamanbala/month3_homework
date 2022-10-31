FROM python:3.10
EXPOSE 5003
RUN mkdir -p /opt/services/bot/Elaman22-3
WORKDIR /opt/services/bot/Elaman22-3

RUN mkdir -p /opt/services/bot/geektech-bot/requirements
ADD requirements.txt /opt/services/bot/Elaman22-3/

COPY . /opt/services/bot/Elaman22-3/

RUN pip install -r requirements.txt
CMD ["python", "/opt/services/bot/geektech-bot/main.py"]