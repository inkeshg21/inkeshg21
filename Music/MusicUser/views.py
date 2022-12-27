from django.shortcuts import render, HttpResponse
from MusicUser.models import Song
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate,logout
def index(request):
    song = Song.objects.all()
    return render(request,'index.html',{'song':song}) 
def songs(request):
    song = Song.objects.all()
    return render(request,'songs.html',{'song':song})
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'login.html')
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1= request.POST["password1"]
        password2= request.POST["password2"]
        name = username
        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = name
        myuser.save()
        return redirect('login')
    return render(request,'signup.html')

def logout(request):
    pass

# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from django.views.generic.list import ListView

# # displaying user information in dashboard
# class DashboardView(LoginRequiredMixin, ListView):
#     model = User
#     template_name = "dashboard.html"
#     context_object_name = "user"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["user"] = self.request.user
#         return context