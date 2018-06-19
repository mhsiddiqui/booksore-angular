from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from views import BookView

router = routers.SimpleRouter()
router.register(r'book', BookView)

urlpatterns = [
    url(r'^', include(router.urls)),
]
