# FORCE_FULL_REBUILD 2026-07-09T15:29:00Z — CORRIDA 08:18 AM PT Jul 9: GN07082026UNIS-1137 (RN-188400) ANTI-ESTADO-VIEJO NORMAL→YELLOW/EN_PROCESO. WMS TASK-5311752 IN_PROGRESS. 21a (1g/7y/13n/0r). 26e.
FROM nginx:1.31-alpine
COPY public/ /usr/share/nginx/html/
COPY public/nginx/feed-no-cache.conf /etc/nginx/conf.d/feed-no-cache.conf
EXPOSE 80
