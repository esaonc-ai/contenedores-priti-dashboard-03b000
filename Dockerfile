# FORCE_REDEPLOY 2026-07-09T19:11:57Z — CORRIDA 12:00 PM PT: 21a (3g/7y/11n/0r). 28e.
FROM nginx:1.31-alpine
COPY public/ /usr/share/nginx/html/
COPY public/nginx/feed-no-cache.conf /etc/nginx/conf.d/feed-no-cache.conf
EXPOSE 80
