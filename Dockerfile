# FORCE_FULL_REBUILD 2026-07-09T18:26:00Z — CORRIDA 11:15 AM PT Jul 9: 3 removals (FFAU2426030 CLOSED, CORR007082026UNIS PO8469 CLOSED, TIIU8088862 SUPERSEDED) + 2 green (CMAU4986523 SPOT2, GN07072026UNIS-1136 DOCK11) + 1 yellow (GN07082026UNIS-1138 DOCK55) + 1 new (TIIU6675500) + 2 RN updates. 19a (3g/6y/10n/0r). 29e.
FROM nginx:1.31-alpine
COPY public/ /usr/share/nginx/html/
COPY public/nginx/feed-no-cache.conf /etc/nginx/conf.d/feed-no-cache.conf
EXPOSE 80
