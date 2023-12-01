#!/bin/bash
# shellcheck shell=bash

umask ${UMASK}

groupmod -o -g "${PGID}" dagent
usermod -o -u "${PUID}" dagent

chown dagent:dagent -R /app /home/dagent

exec su-exec "${PUID}:${PGID}" python3 main.py