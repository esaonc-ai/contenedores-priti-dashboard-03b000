# FORCE_FULL_REBUILD 2026-07-09T17:30:00Z — CORRIDA 10:20 AM PT Jul 9: FFAU2426030 REMOVED (CLOSED). CMAU4986523→GREEN. GN1137/1138→YELLOW. +TIIU6675500. 21a (2g/7y/12n/0r). 27e.
FROM nginx:1.31-alpine
COPY public/ /usr/share/nginx/html/
COPY public/nginx/feed-no-cache.conf /etc/nginx/conf.d/feed-no-cache.conf
EXPOSE 80
