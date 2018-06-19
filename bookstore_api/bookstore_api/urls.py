"""bookstore_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from schema import AllSchemas
from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^auth_service/gql', csrf_exempt(GraphQLView.as_view(
        graphiql=True, schema=AllSchemas.auth_service))),

    url(r'^book_service/gql', csrf_exempt(GraphQLView.as_view(
        graphiql=True, schema=AllSchemas.book_service))),

    url(r'^user_service/gql', csrf_exempt(GraphQLView.as_view(
        graphiql=True, schema=AllSchemas.user_service))),

    # url(r'^auth_service/', include('auth_service.urls')),

    url(r'^book_service/', include('book_service.urls')),

    # url(r'^user_service/', include('user_service.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
