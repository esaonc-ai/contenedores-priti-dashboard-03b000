FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# force rebuild 2026-07-03T21:34:21Z -- Corrida 14:34 PT feed update
# Deploy trigger 1783115459
# force rebuild 2026-07-03T22:25:41Z — Corrida 15:25 PT WMS updates
