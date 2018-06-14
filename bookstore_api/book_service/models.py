# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel
from django.db import models


class Book(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    author = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    user = models.ForeignKey(to=get_user_model(), null=True, blank=True)

    def __str__(self):
        return self.title
