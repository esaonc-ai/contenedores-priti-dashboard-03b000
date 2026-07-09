# FORCE_REDEPLOY 2026-07-09T18:28:24Z — CORRIDA 11:15 AM PT: redeploy trigger. 19a (3g/6y/10n/0r). 29e.
FROM nginx:1.31-alpine
COPY public/ /usr/share/nginx/html/
COPY public/nginx/feed-no-cache.conf /etc/nginx/conf.d/feed-no-cache.conf
EXPOSE 80
