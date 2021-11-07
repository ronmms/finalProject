from django.contrib import admin
from django.urls import path

from md5str.views import generate_new_md5str

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/string/md5string', generate_new_md5str),
]
