from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Experts(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'experts'

class Videos(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    note = models.TextField(blank=True, default='')
    video = models.FileField(upload_to='videos/')
    section = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    expert_id = models.ForeignKey(Experts, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        db_table = 'videos'

class Recipes(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, default='')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Chatbot(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question
    
    class Meta:
        managed = True
        db_table = 'chatbot'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile') 
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Categories(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Products(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    payment_method = models.CharField(max_length=255)
    total = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    address = models.TextField(null=True, blank=True)
    governate = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        managed = True
        db_table = 'orders'

class Orders_items(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.FloatField()
    qty = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'orders_items'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:
        if created:
            Profile.objects.create(user=instance).save()
    except Exception as err:
        print('Error: something happen while creating user profile...')