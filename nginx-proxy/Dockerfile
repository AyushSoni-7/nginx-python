FROM nginx
ARG nginx_conf_filepath=lb_round_robin.conf
RUN rm /etc/nginx/conf.d/default.conf
COPY conf-template/${nginx_conf_filepath}  /etc/nginx/nginx.conf

