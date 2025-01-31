from django.urls import path
from .views import *

urlpatterns = [
    path('', register_and_login, name='index'),
    path('signout/',SignoutView.as_view(),name='signout'),
    path('home/', HomeView.as_view(), name='home'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),

    path('shop/', register_and_login_shop_user, name='register_shop'),
    path('shop/home/', ShopHomeView.as_view(), name='shop_home'),
    path('shop/profile/', ShopProfileCreateView.as_view(), name='shop_profile_create'),
    path('shop/profile/<int:pk>/', ShopProfileDetailsView.as_view(), name='shop_profile_details'),

    path('category/add/', CategoryCreateView.as_view(), name='add_category'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('booking/add/', BookingCreateView.as_view(), name='add_booking'),
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('review/add/', ReviewCreateView.as_view(), name='add_review'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
]
