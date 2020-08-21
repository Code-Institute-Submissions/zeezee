from django.db import models
from django.utils import timezone


# Create your models here.
class Comment(models.Model): 
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 
 
    class Meta: 
        ordering = ('created',) 
 
    def __str__(self): 
       template = loader.get_template("feedback/feedback.html")
       return HttpResponse(template.render)

    