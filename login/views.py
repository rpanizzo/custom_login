from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from pyramid.security import (
    remember,
    forget,
    )
from pyramid.view import (
    view_config,
    view_defaults
    )

from .models import DBSession, User


@view_config(route_name='home')
def home(request):
    # Verifica que haya un usuario loggeado
    if not request.authenticated_userid:
        return HTTPFound(location=request.route_url('login'))
    html = "<!DOCTYPE html>"
    html += "<head><title>Login</title><link href='static/css/style.css' rel='stylesheet'>" \
            "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script></head>" \
            "<script src='static/js/home.js'></script>"
    html += "<body><a href='/logout' class='logout'>Logout</a><h1>Bienvenido <div id='user_name'></h1></body>"
    html += "</html>"
    return Response(html)


@view_config(route_name='get_user_json', renderer='json')
def get_user_json(request):
    if not request.authenticated_userid:
        raise HTTPForbidden
    user = DBSession.query(User).filter_by(name=request.authenticated_userid).one()
    return {'name': user.name}


@view_defaults(renderer="/templates/login.jinja2")
class LoginViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='login')
    def login(self):
        login = self.request.params.get('login')
        password = self.request.params.get('password')
        if self.request.method == 'POST':
            user = DBSession.query(User).filter_by(name=login).first()
            if user and user.check_password(password):
                headers = remember(self.request, login)
                return HTTPFound('/', headers=headers)
            else:
                message = "El Usuario ingresado no es correcto. Intentelo Nuevamente"
                return {'message': message}
        return {}

    @view_config(route_name='logout')
    def logout(self):
        headers = forget(self.request)
        return HTTPFound(location=self.request.route_url('login'), headers=headers)
