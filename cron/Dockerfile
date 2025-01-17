FROM python:alpine
RUN apk --no-cache add dcron
COPY crontab /etc/crontabs/root
RUN mkdir /cron
RUN touch /cron/django_cron.log

WORKDIR /cron
ADD ./requirements.txt /cron/
RUN pip install -r requirements2.txt

CMD ["/bin/sh", "-c", "crond -f && tail -f /dev/null"]