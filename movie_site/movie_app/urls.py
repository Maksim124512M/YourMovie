from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='home'),
    path('signup/', views.RegisterView.as_view(), name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)