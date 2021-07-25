FROM python:3
ENV  PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /backend/

