#!/bin/bash
# shellcheck shell=bash

umask ${UMASK}

groupmod -o -g "${PGID}" dagent
usermod -o -u "${PUID}" dagent

chown dagent:dagent -R /app /home/dagent
chown dagent:dagent /downloads

exec su-exec "${PUID}:${PGID}" python3 main.py