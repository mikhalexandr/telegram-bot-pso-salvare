FROM python:3.11

WORKDIR /main

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

COPY . /main
WORKDIR /main

EXPOSE 5252

CMD ["python3", "main.py"]
