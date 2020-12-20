from django.shortcuts import render,redirect
from django.contrib.auth.models import User #계정을 만들도록 해주는것.
from django.contrib import auth #계정에 대한 권한을 가져오기.

def signup(request):
    if request.method == 'POST': #POST로 받은 회원가입만 처리.
        if request.POST['password1'] == request.POST['password2']: #확인비번이 같은지. 
            user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user) # 회원가입후 자동 로그인.
            return redirect('home') #위 함수를 실행후 home.html로 이동시켜주기.
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username'] #회원가입떄 받은 유저네임 패스워드 변수에 담기.
        password = request.POST['password1']
        user = auth.authenticate(request, username=username, password=password) #authenticate 함수는 데이터베이스에서 회원가입에서 받은 가 맞는 확인해주는 함수.
        if user is not None: #만약 위에 함수에서 회원이 없는 결과가 나오면 출력 아니라면 밑에 실행
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, ' login.html', {'error' : 'username or password is incorrect.'}) #회원이 아니라면 에러.
    else:
        return render(request, 'login.html') #뭔가 고장이나면 그냥 로그인 페이지띄우기.
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')

   

