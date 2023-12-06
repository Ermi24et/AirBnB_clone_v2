#!/usr/bin/env bash
# a script that sets up a web servers for the deployment of web_static.

check_nginx=$(dpkg -l | grep -w nginx -c)

if [ "$check_nginx" -gt 0 ]; then
	:
else
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "<html><head><title>Hello Page</title></head><body><h1>Hello, There</h1></body></html>" > /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "server {
    location /hbnb_static {
        alias /data/web_static/current/;
	index index.html;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
