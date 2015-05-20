from django.db.models import *
from django.utils import timezone

# Create your models here.
class Post(Model):
    author = ForeignKey('auth.User')
    title = CharField(max_length=100)
    text = TextField()
    created_date = DateTimeField(default = timezone.now)
    published_date = DateTimeField(blank = True, null = True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title