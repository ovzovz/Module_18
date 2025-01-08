from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

users = ['user1', 'user2', 'user3']
info = {}
def info_set(username, password, repeat_password, age):
    if password != repeat_password:
        info['error'] = 'Пароли не совпадают'
    if int(age)<18:
        info['error'] ='Вы должны быть старше 18'
    if username in users:
        info['error'] = 'Пользователь уже существует'
    if not info:
        info['new_user'] = username
    return

def sign_up_by_django(request):
    info.clear()
    if request.method == 'POST':
        form=UserRegister(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            repeat_password=form.cleaned_data['repeat_password']
            age=form.cleaned_data['age']
            info_set(username, password, repeat_password, age)
    else:
        form=UserRegister()
    info["form"]=form
    return render(request, 'registration_page.html', context=info)  #{'form':form})

def sign_up_by_html(request):
    info.clear()
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        repeat_password=request.POST.get('repeat_password')
        age=request.POST.get('age')
        info_set(username, password, repeat_password, age)
        return render(request, 'registration_page.html', context=info)
    return render(request, 'registration_page.html')



#info_set('us', 'password','password',17)
#print(info)