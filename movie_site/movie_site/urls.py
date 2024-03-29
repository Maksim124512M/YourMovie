from django.contrib import admin
from django.urls import path, include
from movie_app.views import FilmViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register(r'films', FilmViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_app.urls')),
    path('api/films', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
