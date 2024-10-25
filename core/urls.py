from django.contrib import admin
from django.urls import path, include
from api.views import IndexPage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('api/auth',include('rest_auth.urls')),
    path('',IndexPage),
    path('api/v1/rest_auth/registration',include('rest_auth.registration.urls')),
    path('api/v1/rest_auth/',include('rest_auth.urls'))
]
