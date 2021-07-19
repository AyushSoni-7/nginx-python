ARG nginx_conf_filepath="./conf-template/nginx.conf"

FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY ./conf-template/nginx.conf  /etc/nginx/nginx.conf
