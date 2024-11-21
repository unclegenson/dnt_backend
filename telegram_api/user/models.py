from django.db import models

class UserApp(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=150,null=False)
    user_telid = models.IntegerField(null=False,blank=False,unique=True)
    created_time = models.DateTimeField(auto_now=True)
    referral_count =  models.IntegerField(default=0)
    point = models.IntegerField(default=500)
    # user_image = models.ImageField(upload_to='images/')
      