FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 80
# Force Docker rebuild 2026-07-05T08:38:00Z — Corrida Jul 4 18:33 PT — all 25 containers re-verified against WMS+YMS. Updated lastVerifiedAt, verificationSource, appointmentTime, recvTask/putTask fields. Fresh verification timestamp.
