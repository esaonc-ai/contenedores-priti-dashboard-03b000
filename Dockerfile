FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# Force Docker rebuild 2026-07-04T07:45:42Z -- Corrida 00:33 PT 26activos 6G/8Y/0R/12N -- trigger 1783151142
