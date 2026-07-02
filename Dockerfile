FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# force rebuild 2026-07-02T14:41:58Z -- Deploy CSGU DOCK69 fix + putaway recheck
