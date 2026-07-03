FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# force rebuild 2026-07-03T21:24:11Z -- Corrida 14:22 PT feed update 19 changes
