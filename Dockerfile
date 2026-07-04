FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# Force Docker rebuild 2026-07-04T12:32:00Z -- Corrida 05:23 PT 25activos 6G/7Y/0R/12N -- trigger 1783168320
