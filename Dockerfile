# Dockerfile production example

FROM python:3.8

WORKDIR /app/

RUN pip install --upgrade pip
RUN pip install pipenv

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN pipenv install --deploy --system

COPY . .
