FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# Force Docker rebuild 2026-07-04T18:38:29Z -- Corrida Jul 4 11:38 AM PT 28activos 6G/10Y/0R/12N -- repeat trigger
