from django.db import models

class Portfolio(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __unicode__(self):
        return self.title


