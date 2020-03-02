FROM python:3.7

ENV APP_ROOT /src
ENV CONFIG_ROOT /config

RUN mkdir ${CONFIG_ROOT}
COPY /postal_ranges/requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

RUN mkdir ${APP_ROOT}
RUN mkdir ${APP_ROOT}/static

# copy entrypoint.sh
COPY postal_ranges/entrypoint.sh /config/entrypoint.sh
RUN chmod +x /config/entrypoint.sh

WORKDIR ${APP_ROOT}

ADD /postal_ranges/ ${APP_ROOT}

ENTRYPOINT ["/config/entrypoint.sh"]

