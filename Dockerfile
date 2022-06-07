FROM python:3.8-alpine

RUN pip install openpyxl

WORKDIR /work
ADD create_message.py /work
ADD MessageCd.template.java /work

CMD [ "python3", "create_message.py"]