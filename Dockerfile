FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# force rebuild 2026-07-03T18:51:00Z -- Corrida 11:49 PT feed update
