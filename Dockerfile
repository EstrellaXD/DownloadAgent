# syntax=docker/dockerfile:1

FROM python:3.11-alpine
ENV LANG="C.UTF-8" \
    TZ=Asia/Shanghai \
    PUID=1000 \
    PGID=1000 \
    UMASK=022
WORKDIR /app
COPY requirements.txt .
RUN set -ex && \
    apk add --no-cache \
        bash \
        busybox-suid \
        su-exec \
        shadow \
        tini \
        openssl \
        tzdata && \
    python3 -m pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    # Add user
    mkdir -p /home/dagent && \
    addgroup -S dagent -g 911 && \
    adduser -S dagent -G dagent -h /home/dagent -s /sbin/nologin -u 911 && \
    # Clear
    rm -rf \
        /root/.cache \
        /tmp/*
COPY . .
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["tini", "-g", "--", "/entrypoint.sh"]

ENV CONTAINER=1

VOLUME ["/downloads"]