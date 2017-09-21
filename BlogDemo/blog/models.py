
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
from django.utils.html import strip_tags

from simditor.fields import RichTextField



# Create your models here.

#分类
class Category(models.Model):
	name = models.CharField(max_length=100,verbose_name='分类')


	@python_2_unicode_compatible
	def __str__(self):
		return self.name


#标签
class Tag(models.Model):
	name = models.CharField(max_length=100,verbose_name='标签')

	@python_2_unicode_compatible
	def __str__(self):
		return self.name


#文章
class Post(models.Model):
	title = models.CharField(max_length=80,verbose_name='文章标题')
	body = RichTextField(verbose_name='文章正文')	#富文本编辑器
	#创建时间
	created_time = models.DateTimeField(verbose_name='创建时间')
	#最后一次修改时间
	modified_time = models.DateTimeField(verbose_name='修改时间')
	#文章摘要
	excerpt = models.CharField(max_length=100,blank=True,verbose_name='文章摘要')

	#分类，一对多关系，一篇文章有一个分类，一个分类有多篇文章
	category = models.ForeignKey(Category,verbose_name='分类')
	#标签，多对多关系，一篇文章可以有多个标签
	tags = models.ManyToManyField(Tag,blank=True,verbose_name='标签')
	#作者
	author = models.ForeignKey(User,verbose_name='作者')
	#阅读量字段
	views = models.PositiveIntegerField(default=0)

	@python_2_unicode_compatible
	def __str__(self):
		return self.title

	#这个方法生成url
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})

	#阅读量
	def increase_views(self):
		self.views +=1
		#update_fields 参数来告诉 Django 只更新数据库中 views 字段的值
		self.save(update_fields=['views'])

	#自动生成文章摘要
	# def save(self,*args,**kwargs):
	# 	#如果没有填定摘要
	# 	if not self.excerpt:
	# 		#首先实例化一个 Markdown 类，用于渲染 body 的文本
	# 		md = markdown.Markdown(extensions=[
	# 			'markdown.extensions.extra',
	# 			'markdown.extensions.codehilite',
	# 		])
	# 		# 先将 Markdown 文本渲染成 HTML 文本
	# 		# strip_tags 去掉 HTML 文本的全部 HTML 标签
	# 		# 从文本摘取前 54 个字符赋给 excerpt
	# 		self.excerpt = strip_tags(md.convert(self.body))[:54]
	# 	# 调用父类的 save 方法将数据保存到数据库中
	# 	super(Post, self).save( *args, **kwargs )

	class Meta:
		ordering = ['-created_time']