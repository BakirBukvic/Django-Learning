from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class item(models.Model):


    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200, default='Default')
    item_desc = models.CharField(max_length=200, default='Default')
    image_url = models.CharField(max_length=500, default ='https://cdn-icons-png.flaticon.com/512/1377/1377194.png')
    item_price = models.IntegerField()


    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk":self.pk})