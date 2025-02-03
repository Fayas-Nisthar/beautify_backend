from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password,check_password
from django.db.models.signals import post_save

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
    
class ShopUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class UserProfileModel(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    contact=models.CharField(max_length=12,null=True)
    pic=models.ImageField(upload_to="pro_pic",null=True,blank=True,default='pro_pic/avatar_2.png')
    def __str__(self):
        return self.user.first_name

class CategoryModel(models.Model):
    image=models.ImageField(upload_to="cat_img",null=True,blank=True)
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type

class ShopProfileModel(models.Model):
    shop=models.OneToOneField(ShopUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=12)
    pic=models.ImageField(upload_to="shop_pic",default='shop_pic/shop.jpg')
    activity=models.BooleanField(default=False)
    location=models.CharField(max_length=200)
    gender_options=(
        ("Unisex","Unisex"),
        ("Men","Men"),
        ("Women","Women"),
    )
    preferredGender=models.CharField(max_length=10,choices=gender_options)
    category=models.ManyToManyField(CategoryModel)
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

