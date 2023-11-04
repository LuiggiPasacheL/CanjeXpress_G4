FROM nginx:1.25.3

COPY . /etc/nginx/conf.d
COPY entrypoint.sh /docker-entrypoint.d/entrypoint.sh

CMD ["nginx", "-g", "daemon off;"]
