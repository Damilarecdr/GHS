
from django.db import models
from django.core.validators import FileExtensionValidator

class Slide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/slides/', blank=True, null=True) 
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
class Update(models.Model):
    news = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.news

class HAbout(models.Model):
    title = models.CharField(max_length=200)
    welcome_address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/images/habout/', blank=True, null=True) 

    def __str__(self):
        return self.title

class Hadmission(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    link = models.URLField()
    video = models.FileField(upload_to='uploads/videos',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    #image = models.ImageField(upload_to='slides/', blank=True, null=True) 

    def __str__(self):
        return self.heading

class Whyu(models.Model):
    heading = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    #icon = models.ImageField(upload_to='icon/', blank=True, null=True) 

    def __str__(self):
        return self.heading

class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    t_id = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/teachers/images/', blank=True, null=True) 
    def __str__(self):
        return self.full_name

class Logo(models.Model):
    img =  models.ImageField(upload_to='uploads/logo/images/', blank=True, null=True) 
    img2 =  models.ImageField(upload_to='uploads/logo/images/', blank=True, null=True) 
    school_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    facebook =  models.URLField(blank=True, null=True)
    youtube =  models.URLField(blank=True, null=True)
    instagram =  models.URLField(blank=True, null=True)


