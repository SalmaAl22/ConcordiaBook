from django.db import models

class Textbook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=50, null=True, blank=True)
    condition = models.CharField(max_length=50)  
    course_code = models.CharField(max_length=20)
    available = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.title} by {self.author} for {self.course_code}"