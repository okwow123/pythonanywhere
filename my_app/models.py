# -*- coding: utf-8 -*- 
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

class Post(models.Model):
    print "Post model call"
    author = models.ForeignKey('auth.User',default='')
    no = models.AutoField(primary_key=True)
    category=models.CharField(max_length=200,default='test')
    title = models.CharField(max_length=200)
    content = models.TextField(default='',null=True)
    good_count = models.IntegerField(default=0)
    images= models.ImageField(upload_to='./my_app/static/upload',default=None,null=False)
    #created_date = models.DateTimeField(
    #        default=timezone.now)
    #published_date = models.DateTimeField(
    #        blank=True, null=True)
    def publish(self):
        #self.published_date = timezone.now()
        self.save()

    #def __str__(self):
    def __Unicode_(self):
        return self.title


    def image_tag(self):
        images=self.images
	strImages=str(images)
	strImages=strImages[6:]
        return mark_safe('<img src="%s" width="150" height="150" />' % (strImages))

    image_tag.short_description = 'Image'
