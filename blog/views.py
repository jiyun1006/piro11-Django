from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
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

def post_detail(request, id):
    # try:
    #
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(Post,id=id)

    return render(request, 'blog/post_detail.html',
                  {
                      'post' : post,
                  })