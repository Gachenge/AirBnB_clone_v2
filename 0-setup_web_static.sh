#!/usr/bin/env bash
# set up web servers for deployment of web_static

apt update
apt install -y nginx

mkdir -p /data/web_static/releases/test
mkdir /data/web_static/shared

echo "Hello World" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data

printf %s "server {
    listen  80 default_server;
    listen  [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root    /etc/nginx/html;
    index   index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
    }
    
    location /redirect_me {
        return 301 http://alx.com/;
    }
    error_page 404 /custom.html;
    location = /custom {
        root /etc/nginx/html;
        internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
