# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/git-ctf-website

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev git
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/git-ctf-website/entrypoint.sh
RUN chmod +x /usr/src/git-ctf-website/entrypoint.sh

# copy project
COPY . .

ENTRYPOINT ["sh", "/usr/src/git-ctf-website/entrypoint.sh"]
