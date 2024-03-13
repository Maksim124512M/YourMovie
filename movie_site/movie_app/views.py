from rest_framework.viewsets import ModelViewSet 
from django.shortcuts import render
from .forms import UserSignupForm, CommentForm
from django.urls import reverse_lazy
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.views.generic import FormView
from .serializers import FilmSerializer
from .models import Film, Comment


class RegisterView(FormView):
    form_class = UserSignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
def home(request):
    film = Film.objects.all()


    context = {
        'film': film,
    }
    return render(request, 'home.html', context)

def film(request, id):
    film = Film.objects.filter(id=id)
    form = CommentForm()
    user_model = User.objects.all()
    comment_model = Comment.objects.all()

    

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'film': film,
        'form': form,
        'user': user_model,
        'comment': comment_model,
    }
    return render(request, 'film.html', context)

class FilmViewSet(ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all().order_by('name')
    permission_classes = (IsAdminUser)