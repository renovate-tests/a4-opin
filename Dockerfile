FROM alpine:3.5

RUN apk add --no-cache python3 nodejs build-base jpeg-dev zlib-dev git python3-dev libffi-dev libmagic

WORKDIR /var/env

# install dependencies
ADD ./package.json /var/env
RUN npm install
ADD ./requirements /var/env/requirements
RUN python3 -m venv .
RUN bin/python3 -m pip install -r ./requirements/aws.txt
RUN bin/python3 -m pip install gunicorn

# install our code
WORKDIR /var/env/app
ADD . /var/env/app
RUN npm build
RUN bin/python3 ./manage.py collectstatic --noinput

EXPOSE 6000
ENTRYPOINT /var/app/bin/gunicorn \
               --env DJANGO_SETTINGS_MODULE=euth_wagtail.settings.aws \
               --forwarded-allow-ips=* \
               --bind=0.0.0.0:6000 \
               --workers=2 \
               --name=euth_wagtail \
               euth_wagtail.wsgi
