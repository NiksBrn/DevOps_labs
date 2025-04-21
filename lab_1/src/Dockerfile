FROM alpine:3.21

RUN apk add --no-cache nginx
RUN addgroup -g 1122 nginxuser_g && \
      adduser -D -u 1122 -G nginxuser_g nginxuser
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./html /var/data/html
RUN chown -R nginxuser:nginxuser_g \
      /var/data \
      /var/log/nginx \
      /var/run/nginx \
      /var/lib/nginx
RUN chmod -R 755 \
      /var/data \
      /var/log/nginx \
      /var/run/nginx \
      /var/lib/nginx

EXPOSE 8080
USER nginxuser:nginxuser_g
CMD ["nginx", "-g", "daemon off;"]