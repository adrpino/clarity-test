FROM python:3.9


ENV APP_HOME /opt/clarity-assessment/

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN pip install pipenv
ADD Pipfile* $APP_HOME

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

ADD . $APP_HOME

ADD start.sh /start

EXPOSE 5000

CMD [ "/start" ]
