from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.db.models.signals import post_save

# Create your models here.

class UserModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class ShopModel(models.Model):
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class UserProfileModel(models.Model):
    user=models.OneToOneField(UserModel,on_delete=models.CASCADE)
    contact=models.CharField(max_length=12,null=True)
    pic=models.ImageField(upload_to="pro_pic",null=True,blank=True,default='pro_pic/avatar_2.png')
    def __str__(self):
        return self.first_name

class CategoryModel(models.Model):
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type

class ShopProfileModel(models.Model):
    shop=models.OneToOneField(ShopModel,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    contact=models.CharField(max_length=12)
    pic=models.ImageField(upload_to="shop_pic",default='shop_pic/shop.jpg')
    activity_options=(
        ("Available","Available"),
        ("Offline","Offline"),
    )
    activity=models.CharField(max_length=30,choices=activity_options,default="Offline")
    location=models.CharField(max_length=200)
    gender_options=(
        ("Unisex","Unisex"),
        ("Men","Men"),
        ("Women","Women"),
    )
    preferredGender=models.CharField(max_length=10,choices=gender_options)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Booking(models.Model):
    user=models.ForeignKey(UserProfileModel,on_delete=models.CASCADE,related_name="booked_user")
    shop=models.ForeignKey(ShopProfileModel,on_delete=models.CASCADE,related_name="booked_shop")
    date=models.DateTimeField(auto_now_add=True)
    options=(
        ("Pending","Pending"),
        ("Accept","Accept"),
        ("Reject","Reject"),
    )
    status=models.CharField(max_length=100,choices=options,default="Pending")

    def __str__(self):
        return self.shop

class Review(models.Model):
    user=models.ForeignKey(UserProfileModel,on_delete=models.CASCADE,related_name="reviwed_user")
    shop=models.ForeignKey(ShopProfileModel,on_delete=models.CASCADE,related_name="reviwed_shop")
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))

    def __str__(self):
        return self.rating

def create_profile(sender,created,instance,**kwargs):
    if created:
        UserProfileModel.objects.create(user=instance)
post_save.connect(create_profile,sender=UserModel)