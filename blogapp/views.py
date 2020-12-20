from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator 
from .models import Blog
from .form import BlogPost
# Create your views here.
def home(request):
    blogs = Blog.objects #쿼리셋 = 모델로부터 전달받는 객체들을 가져오는 것.
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page') # ('이곳에는 딕셔너리 형으로 해줘야함.')
    #request된 페이지를 얻어온뒤 return 해줌. 
    posts = paginator.get_page(page)
    return render(request,'home.html', {'blogs': blogs, 'posts' : posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'details' :details})

def new(request): #new.html을 띄워주는함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog =Blog() #blog 객체 생성
    blog.title = request.GET['title'] #요청받은 데이터를 blog.title에 넣어주기. 
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() #블로그 작성을 한 시간.
    blog.save() #쿼리셋 메소드 데이터베이스에 저장시키는 함수.
    return redirect( '/blog/' + str(blog.id))
    # 위에 리다이렉트에 () 안에는 밖의 주소를 써도된다 ex: 구글.com 을 쓰면 함수실행 후 구글.com 으로 이동

    #쿼리셋 메소드 형식
    #모델.쿼리셋(object).메소드 

def blogpost(request):
    # 1. 입력된 내용 처리하기 -> POST 방식
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid(): #form 에서 값이 제대로 입력됐는지 체크하는 함수.
            post = form.save(commit =False) #블로그 객체를 가져오되, 아직은 저장하지 말기.
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 2. 빈 페이지를 띄워주는 기능 -> GET 방식
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form': form})
