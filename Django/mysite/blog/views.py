from django.shortcuts import render
from .models import Post
from django.core.paginateor import Paginator # 페이징 처리를 위한 클래스
# 페이징 처리 -> 한 페이지에 보여줄 게시글의 수를 지정하고,

# 홈화면 -> 최근 게시물 5개가 있는 구조
def home(request):
    recent_post = Post.objects.order_by('-created_date')[:5]
    return render(request, 'blog/home.html', {'recent_post': recent_post})

#post_list -> 모델에서 게시글을 가져오는 함수
def post_list(request):
    post_list = Post.objects.all().order_by('-created_date')
    paginator = Paginator(post_list, 1) # 한 페이지에 1개의 게시글을 보여줌
    
    page = request.GET.get('page') # 페이지 번호를 가져오는 함수
    # 페이지 번호를 URL의 쿼리스트링에서 가져오는 함수 예를 들어 ?page=2 두번째 페이지를 가져오게 함
    # 객체에서 현재 페이지의 게시글을 가져오는 함수 
	# -> 유효하지 않은 페이지 번호를 입력하면 기본적으로 첫번째  게시글을 가져오도록 수행
    posts = paginator.get_page(page) # 해당 페이지의 게시글을 가져오는 함수
    
    return render(request, 'blog/post_list.html', {'posts': posts})

# home 뷰는 요청이 들어오면 최근에 작성된 5개의 포스트를 홈페이지에서 보여줌
# recent_post -> 모델에서 가장 최근에 작성된 5개의 게시글을 가져오는
# render 템플릿을 활용해 응답을 생성 -> request 요청하는 객체, blog/home.html 템플릿 파일,
# recent_post 모델에서 가져온 데이터


