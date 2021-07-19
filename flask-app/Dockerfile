FROM python:3.7-alpine
WORKDIR app
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "-u", "main.py" ]

