FROM python:3.5

MAINTAINER Rafael Abreu <abreu@gorillascode.com>

RUN pip install gunicorn --upgrade pip

ADD . /gorillassite

RUN mkdir -p /gorillassite/logs

WORKDIR /gorillassite

# RUN python setup.py install

ADD requirements.txt /
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--config=gunicorn.py", "run:app"]
