from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION',max_length=100, blank=True,help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE',auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY_DATE',auto_now=True)
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts' #plural은 복수명칭, 여러개있다면 posts
        db_table = 'blog_posts'
        ordering = ('-modify_dt',) #수정일자를 내림차순으로 (-), 튜플형태로 지정(), 여러개가 들어갈 수 있으니 콤마를 찍어줌
        
    def __str__(self): #객체를 표현하는 방식
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=(self.slug,))
    
    def get_previous(self): #이전으로 가기
        return self.get_previous_by_modify_dt()
    
    def get_next(self): #이후로 가기
        return self.get_next_by_modify_dt()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
        
        