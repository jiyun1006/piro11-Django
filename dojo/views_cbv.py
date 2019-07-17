from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse

class PostList1View1(View):
    def get(self, request):
        name= '공유'
        html = self.get_template_string().format(name=name)

        return HttpResponse(html)

    def get_template_string(self):
        return '''
     <h1>AskDjango<h1>
        <p>{name}<p>
        <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
    '''


post_list1 = PostList1View1.as_view()


class PostList2View2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_content_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context


post_list2 = PostList2View2.as_view()



class PostList3View3(object):
    pass




class ExcelDownloadView(TemplateView):
    pass 
