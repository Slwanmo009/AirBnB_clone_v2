#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static.

# Install Nginx if it is not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get install -y nginx
fi

# Create the necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Hello World
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
CONFIG_FILE='/etc/nginx/sites-available/default'
if ! grep -q 'location /hbnb_static' $CONFIG_FILE; then
    sed -i '/server_name _;/a \\
    location /hbnb_static/ {\\n\
        alias /data/web_static/current/;\\n\
    }' $CONFIG_FILE
fi

# Restart Nginx
service nginx restart
