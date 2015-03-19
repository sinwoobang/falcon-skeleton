# -*- coding:utf-8 -*-
from wsgiref import simple_server

from app import create_app


# Set up falcon api
app = application = create_app()


if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 5000, app)
    httpd.serve_forever()

