FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# Force Docker rebuild 2026-07-04T20:51:41Z — Corrida Jul 4 13:51 PT 25activos 6G/7Y/12N — RN-188094 removido
