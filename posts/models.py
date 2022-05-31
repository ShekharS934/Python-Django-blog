from django.db import models

# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=255)
    pub_dt=models.DateTimeField()
    img=models.ImageField(upload_to='media/')
    body=models.TextField()
    
    def __str__(self):   #to print the title on the posts screen instead of post1, post2 and so on.
        return self.Title
    
    def pub_date(self):   #to get the date according to user
        return self.pub_dt.strftime('%b %d %Y')
    
    def summary(self):   #to limit the characters in a post to display on homepage
        return self.body[:100]