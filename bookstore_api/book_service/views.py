# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from models import Book
from serializer import BookSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    permission_classes = []
    authentication_classes = []
