FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# force rebuild 2026-07-02T03:00:49Z -- Deploy URGENTE feed 19:50 PT
