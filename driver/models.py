from django.db import models
from django.contrib.auth.models import User
import qrcode
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    user =  models.OneToOneField(User,models.CASCADE)
    name_of_driver  = models.CharField(max_length=250, blank=True,null=True)
    email_address = models.EmailField()
    address = models.CharField(max_length=14,blank=True,null=True)
    city = models.CharField(max_length=250, blank=True,null=True)
    phone_number = models.CharField(max_length=14,blank=True,null=True)
    date_of_birth=models.DateTimeField()
    educational_background = models.CharField(max_length=250, blank=True,null=True)
    state_of_origin = models.CharField(max_length=250, blank=True,null=True)
    local_government =models.CharField(max_length=250, blank=True,null=True)
    blood_group= models.CharField(max_length=250, blank=True,null=True)
    height=models.CharField(max_length=250, blank=True,null=True)
    any_form_of_disability = models.CharField(max_length=250, blank=True,null=True)
    nationality = models.CharField(max_length=250, blank=True,null=True)
    next_of_kin = models.CharField(max_length=250, blank=True,null=True)
    next_of_kin_phone_number = models.CharField(max_length=250, blank=True,null=True)
    uploadedImage =  models.ImageField(upload_to = 'Upload/',blank=False,null=True)
    previous_number =models.CharField(max_length=250, blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)


    # def save(self, *args, **kwargs):
    #     qr = qrcode.QRCode(
    #         version=1,
    #         box_size=15,
    #         border=5
    #     )
    #     qr = qrcode.add_data(self.name_of_driver)
    #     qr = qrcode.add_data(self.email_address)
    #     qr = qrcode.add_data(self.address)
    #     qr = qrcode.add_data(self.city)
    #     qr = qrcode.add_data(self.phone_number)
    #     qr = qrcode.add_data(self.nationality)
    #     qr = qrcode.add_data(self.state_of_origin)
    #     qr = qrcode.add_data(self.local_government)
    #     img = qr.make_image()
    #     img.save("Details.png")
    #     super(Model, self).save(*args, **kwargs)


# @receiver(post_save, sender=User)
# def update_driver_signal(sender, instance, created, **kwargs):
#     if created:
#         Driver.objects.create(user=instance)
#     instance.driver.save()


class FieldNumber(models.Model):
    driver =models.OneToOneField(Driver,models.CASCADE)
    state_of_issuance = models.CharField(max_length=250, blank=True,null=True)
    class_of_liscense= models.CharField(max_length=250, blank=True,null=True)
    number_of_replacement = models.CharField(max_length=250, blank=True,null=True)
    license_of_number = models.CharField(max_length=250, blank=True,null=True)
    chassess_number = models.CharField(max_length=250, blank=True,null=True)
    plate_number =models.CharField(max_length=250, blank=True,null=True)
    expiry_date = models.DateTimeField()
    flag = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)


