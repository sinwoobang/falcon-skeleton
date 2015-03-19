# -*-coding:utf-8-*-
import falcon

# from .middleware import *
from .resources import IndexResource

indexResource = IndexResource()


def create_app():
    app = falcon.API(middleware=[])

    app.add_route('/', indexResource)
    app.add_route('/index', indexResource)

    return app