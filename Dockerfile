FROM docker/python:3.9


ENV APP_HOME /opt/clarity-assessment/

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN pip install pipenv
ADD Pipfile* $APP_HOME
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt


EXPOSE 5000

ENTRYPOINT [ "/entrypoint" ]
CMD [ "/start" ]
