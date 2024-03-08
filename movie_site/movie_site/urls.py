from django.contrib import admin
from django.urls import path, include
from movie_app.views import FilmViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'films', FilmViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_app.urls')),
    path('api/films', include(router.urls)),
]

