from django.db import models

# Create your models here.



class Driver(models.Model):
    '''
    name
    naptionality
    experience
    gender
    lisence
    r code 
    '''
    name_of_driver  = models.CharField(max_length=250, blank=True,null=True)
    uploadedImage =  models.ImageField(upload_to = 'Upload/',blank=False,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)

