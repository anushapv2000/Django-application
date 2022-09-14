from django.urls import re_path
from lib import views

urlpatterns = [
    re_path(r'^library$',views.libraryview),
    re_path(r'^library/([0-9]+)$',views.libraryview)

]
