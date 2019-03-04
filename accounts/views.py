from django.shortcuts import render, redirect
from django.contrib.auth.models import User # 유저에 대한 기능
from django.contrib import auth # 계정에 대한 권한

# Create your views here.

def signup(request):
    if request.method == 'POST':
        # 회원가입시 입력한 비밀번호와 재입력 비밀번호 확인하고 맞다면 로그인함수 실행
        if request.POST['password'] == request.POST['confirmpass']:
            user = User.objects.create_user( username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)            
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # 로그인을 시도할시 데이터베이스에 저장된 정보와 일치하는지 확인하고 결과를 user에 담음 (아니면 none)
        user = auth.authenticate(request, username=username, password=password)
                
        # 결과가 맞을시 로그인함수 실행. 아니면 메세지를 출력하며 거부.
        if user is not None:
            auth.login(request, user)   
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:        
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':        
        # auth.logout(request)        
        # # 로그아웃하고 홈으로 돌아가기        
        return redirect('home')
    else:
        auth.logout(request)
        return render(request, 'login.html')
