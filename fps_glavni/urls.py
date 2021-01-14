# -*- coding: utf-8 -*-

from django.urls import path
from .views import IndexView, PartyView, ImpressumView, JsonDbDump

app_name = 'fps_glavni'

urlpatterns = [
    path('', IndexView.as_view(), name="fps_index"),
    path('stranka/<slug:slug>', PartyView.as_view(), name="fps_party"),
    path('impressum/', ImpressumView.as_view(), name="fps_impressum"),
    path('database-dump/', JsonDbDump.as_view(content_type='application/json'), name="database_dump"),
]
