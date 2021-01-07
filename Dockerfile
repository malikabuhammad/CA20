FROM python:3.7-alpine
RUN mkdir /blog
WORKDIR /b.0000000000




















ADD requirements.txt .
RUN pip3 install -r requirements.txt
COPY app/ .
ENTRYPOINT ["sh"]