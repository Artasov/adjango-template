from django.urls import path

from apps.core.controllers.base import example, async_example

urlpatterns = [
    path('example/', example),
    path('aexample/', async_example),
]
