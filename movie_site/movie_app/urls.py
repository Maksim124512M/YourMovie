from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('film/<int:id>', views.film, name='film'),
    path('accounts/signup/', views.RegisterView.as_view(), name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)