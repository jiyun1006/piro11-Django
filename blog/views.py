from django.shortcuts import render
from .models import Post
# def post_list(request):
#     return render(request,'blog/post_list.html')

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q)
    #     q가 포함된 db자료만 검색해서 나타내도록
    return render(request, 'blog/post_list.html',{
        'post_list': qs,
        'q':q
    })