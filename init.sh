sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn_django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart
