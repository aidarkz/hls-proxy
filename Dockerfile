FROM nginx:stable

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /var/cache/nginx/hls_cache \
    && chown -R nginx:nginx /var/cache/nginx
