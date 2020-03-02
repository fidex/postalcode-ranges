FROM python:3.7

ENV APP_ROOT /src
ENV CONFIG_ROOT /config

RUN mkdir ${CONFIG_ROOT}
COPY /postal_ranges/requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

RUN mkdir ${APP_ROOT}
RUN mkdir ${APP_ROOT}/staticfiles
WORKDIR ${APP_ROOT}

ADD /postal_ranges/ ${APP_ROOT}
