# pull official base image
FROM python:3.8.0-alpine

ENV PYTHONUNBUFFERED 1

# Requirements are installed here to ensure they will be cached.
RUN ls -lrt
RUN mkdir /code
WORKDIR /code
COPY /postal_ranges/requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# copy entrypoint.sh
# COPY /entrypoint.sh /app/entrypoint.sh
# RUN chmod +x entrypoint.sh

# COPY ./compose/local/django/start /start
# RUN sed -i 's/\r$//g' /start
# RUN chmod +x /start

# ENTRYPOINT ["/entrypoint.sh"]
