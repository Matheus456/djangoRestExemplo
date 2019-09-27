from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^', include('myapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', obtain_jwt_token),
]