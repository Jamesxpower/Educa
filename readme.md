第 12 章 Building an E-Learning Platform

Source code
    https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter12


第 13 章 Creating a Content Management System

Source code
    https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter13


第 14 章 Rendering and Caching Content

Source code
    https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter14

第 15 章 Building an API
    soruce code 
    https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter15


第 16 章 Building a Chat Server
    source code
    https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter16

第 17 章 Going Live
    source code
    https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter17


django-braces API
https://django-braces.readthedocs.io/en/latest/


HTML5 Sortable library public CDN
https://cdnjs.cloudflare.com/ajax/libs/html5sortable/0.13.3/html5sortable.min.js


django-embed-video is a third-party Django application that allows you to 
embed videos in your templates
https://django-embed-video.readthedocs.io/en/latest/

    pip install django-embed-video
	
	
	
Installing the Memcached Docker image
    docker pull memcached

    docker run -it --rm --name memcached -p 11211:11211 memcached -m 64	

Installing the Memcached Python binding
    pip install pymemcache


Install Django Debug Toolbar
    pip install django-debug-toolbar

Redis
    docker run -it --rm --name redis -p 6379:6379 redis

    Install redis-py
        pip install redis

Django Redisboard (Monitor Redis server)
    https://github.com/ionelmc/django-redisboard

    pip install django-redisboard

    pip install attrs

Django REST framework
    https://www.django-rest-framework.org/

    Install the framework
    pip install djangorestframework

Django Channels
    https://channels.readthedocs.io/en/latest/


Installing Channels
    pip install channels

Installing Channels Redis
    pip install channels-redis


curl for windows
    download
    https://curl.se/windows/
 
Introduction to ASGI
    https://asgi.readthedocs.io/en/latest/introduction.html


Tutorial Part 2: Implement a Chat Server
    https://channels.readthedocs.io/en/stable/tutorial/part_2.html

Daphne ASGI Server
    https://github.com/django/daphne


Creating an SSL/TLS certificate
    openssl req -x509 -newkey rsa:2048 -sha256 -days 3650 -nodes -keyout ssl/educa.key -out ssl/educa.crt -subj '/CN=*.educaproject.com' -addext 'subjectAltName=DNS:*.educaproject.com'

test:test123456
test2:test2123456

docker:
    root:123456
