FROM alpine:3.5

RUN apk add --no-cache python3 nodejs build-base jpeg-dev zlib-dev git python3-dev libffi-dev libmagic

ENV appdir /var/app
WORKDIR ${appdir}

# install dependencies
ADD ./package.json ${appdir}
RUN npm install --production
ADD ./requirements ${appdir}/requirements
RUN python3 -m venv .
RUN bin/python3 -m pip install -r ./requirements/aws.txt
RUN bin/python3 -m pip install gunicorn

# install our code
ADD . ${appdir}
RUN npm build
RUN ${appdir}/bin/python3 ./manage.py collectstatic --noinput

EXPOSE 6000
ENTRYPOINT ${appdir}/bin/gunicorn \
               --env DJANGO_SETTINGS_MODULE=euth_wagtail.settings.aws \
               --forwarded-allow-ips=* \
               --bind=0.0.0.0:6000 \
               --workers=2 \
               --name=euth_wagtail \
               euth_wagtail.wsgi
