from django.shortcuts import render,get_object_or_404
from django.db.models.aggregates import Count
from django.views.generic import ListView,DetailView,View

from .models import Post,Category,Tag

from pure_pagination.mixins import PaginationMixin

import markdown

# Create your views here.

#主页
class IndexView(PaginationMixin,ListView):
   '''
   获得文章列表
   :param request:
   :return:
   '''
   #将 model 指定为 Post，告诉 Django 我要获取的模型是 Post
   model = Post
   #指定这个视图渲染的模板
   template_name = 'blog/index.html'
   #指定获取的模型列表数据保存的变量名。这个变量会被传递给模板。
   context_object_name = 'post_list'
   # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
   paginate_by = 5

    #在ListView中做查询结果分页
   def get_queryset(self):
       if 'q' in self.request.GET:
           return Post.objects.filter(title__icontains=self.request.GET['q'])
       return super(IndexView, self).get_queryset()

   # # #object = Post


# def index(request):
#     post_list = Post.objects.all()
#     return render(request, 'blog/index.html', context={'post_list': post_list})


#详情页
# def detail(request,pk):
#    '''
#    取得页面传递的文章id，然后取得文章的详细信息
#    :param request:
#    :param pk:
#    :return:
#    '''
#    post = get_object_or_404(Post,pk=pk)
#    #阅读量+1
#    post.increase_views()
#
#    post.body = markdown.markdown(post.body,extensions=[
#       'markdown.extensions.extra',
#       'markdown.extensions.codehilite',
#       'markdown.extensions.toc',
#                      ])
#    return render(request,'blog/detail.html',context={'post':post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self,request,*args,**kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView,self).get(request,*args,**kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()
        #视图必须返回一个 HttpResponse 对象
        return response

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        context['post_list'] = Category.objects.all()
        return context

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post


#归档
def archives(request,year,month):
   '''
   取得文章发布的日期(年月)
   :param request: 
   :param year: 
   :param month: 
   :return: 
   '''
   post_list = Post.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
   return render(request,'blog/index.html',{'post_list':post_list})


#归档
class ArchivewView(ListView):
    model = Post
    template_name = 'blog/archives.html'
    context_object_name = 'post_list'

    # def get_queryset(self):
    #     year = self.kwargs.get('year')
    #     month = self.kwargs.get('month')
    #     return super(ArchivewView,self).get_queryset().filter(created_time__year=year,created_time__month=month)


#分类
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})


#分类
class CategoryView(IndexView):
   '''
   取得文章的ID，查询出分类的信息
   在类视图中，从 URL 捕获的命名组参数值保存在实例的 kwargs 属性（是一个字典）里，非命名组参数值保存在实例的 args 属性（是一个列表）里。
   所以用了 self.kwargs.get('pk') 来获取从 URL 捕获的分类 id 值。然后调用父类的 get_queryset 方法获得全部文章列表，
   紧接着就对返回的结果调用了 filter 方法来筛选该分类下的全部文章并返回
   因为CategoryView类中指定的属性值和 IndexView 中是一模一样的，可以直接继承IndexView
   '''
   model = Post
   template_name = 'blog/index.html'
   context_object_name = 'post_list'

   def get_queryset(self):
       cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
       return super(CategoryView,self).get_queryset().filter(category=cate)


#搜索
def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request,'blog/index.html',{'error_msg':error_msg})
    post_list = Post.objects.filter(title__icontains=q)
    return render(request,'blog/index.html',{'error_msg':error_msg,'post_list':post_list})

#标签云
class TagView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super(TagView,self).get_queryset().filter(tags=tag)


