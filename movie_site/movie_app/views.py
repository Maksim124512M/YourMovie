from rest_framework.viewsets import ModelViewSet 
from django.shortcuts import render
from .forms import UserSignupForm
from django.urls import reverse_lazy
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.views.generic import FormView
from .serializers import FilmSerializer
from .models import Film


class RegisterView(FormView):
    form_class = UserSignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
def index(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

class FilmViewSet(ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all().order_by('name')
    permission_classes = (IsAdminUser,)