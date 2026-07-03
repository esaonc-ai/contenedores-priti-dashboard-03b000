FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# force rebuild 2026-07-03T20:00:31Z -- Corrida 12:53 PT feed update
