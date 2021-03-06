from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User # 引用默认的User模型

# Create your models here.
# 默认情况下，每个模型都有一个自增整数字段，名为id，这个字段自动分配，用作主键
class Category(models.Model):   #继承基类django.db.models.Model
    name = models.CharField(max_length=128, unique=True)    #Char unique=True意味着字段的值在模型对应的底层数据库表中必须是唯一的，即可用作主键
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)   # 别名字段

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'  #指定模型的复数形式是什么

    def __str__(self):  #类似于Java中的toString()方法
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()     #类似于Char 不过是专用于存储URL
    views = models.IntegerField(default=0)      #访问次数，存储整数

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # 这一行是必须的
    # 建立与 User 模型之间的关系
    user = models.OneToOneField(User)

    # 想增加的属性
    website = models.URLField(blank=True)   # 可以为空
    picture = models.ImageField(upload_to='profile_images', blank=True)  # 可以为空

    # 覆盖 __str__() 方法，返回有意义的字符串
    def __str__(self):
        return self.user.username