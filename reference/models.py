from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class Reference(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    description = models.CharField(max_length=250)
    link = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'references')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('reference:reference_list')
