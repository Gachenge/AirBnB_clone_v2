#!/usr/bin/env bash
# set up web servers for deployment of web_static

sudo apt update
sudo apt install -y nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir /data/web_static/shared

echo "Hello World" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo printf %s "server {
    listen  80 default_server;
    listen  [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root    /etc/nginx/html;
    index   index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
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

sudo service nginx restart
