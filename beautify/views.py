from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import *
from .models import *

def register_and_login(request):
    if request.method == 'POST':
        reg_form = CustomUserRegistrationForm(request.POST)
        login_form = UserLoginForm(request, data=request.POST)
        if 'register' in request.POST and reg_form.is_valid():
            reg_form.save()
            email = reg_form.cleaned_data.get('email')
            password = reg_form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
        elif 'login' in request.POST and login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
    else:
        reg_form = CustomUserRegistrationForm()
        login_form = UserLoginForm()

    return render(request, 'index.html', {
        'reg_form': reg_form,
        'login_form': login_form,
    })


class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect ("index")
       
class HomeView(View):
    def get(self,request,*args,**kwargs):
        shops=ShopProfileModel.objects.all()
        return render(request,'home.html',{'shops': shops})

class UserProfileUpdateView(UpdateView):
    model = UserProfileModel
    form_class = UserProfileForm
    template_name = 'user_profile.html'
    success_url = reverse_lazy('profile')

# ======== shop ===========
def register_and_login_shop_user(request):
    if request.method == 'POST':
        reg_form = ShopUserRegistrationForm(request.POST)
        login_form = UserLoginForm(request, data=request.POST)
        if 'register' in request.POST and reg_form.is_valid():
            reg_form.save()
            email = reg_form.cleaned_data.get('email')
            password = reg_form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('shop_profile_create')
        elif 'login' in request.POST and login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('shop_home')
    else:
        reg_form = ShopUserRegistrationForm()
        login_form = UserLoginForm()

    return render(request, 'shopregister.html', {
        'reg_form': reg_form,
        'login_form': login_form,
    })

class ShopProfileCreateView(View):
    def get(self, request):
        form = ShopProfileForm()
        return render(request, 'shop_profile.html', {'form': form})

    def post(self, request):
        form = ShopProfileForm(request.POST, request.FILES)
        if form.is_valid():
            shop_profile = form.save(commit=False)
            shop_profile.shop = request.user.shopuser
            shop_profile.save()
            form.save_m2m()
            return redirect('shop_home')
        else:
            print(form.errors)
        return render(request, 'shop_profile.html', {'form': form})

class ShopProfileDetailsView(View):
    def get(self, request, pk):
        shop_profile = get_object_or_404(ShopProfileModel, shop_id=pk)
        form = ShopProfileForm(instance=shop_profile)
        return render(request, 'shop_profile_details.html', {'form': form})

    def post(self, request, pk):
        shop_profile = get_object_or_404(ShopProfileModel, pk=pk)
        form = ShopProfileForm(request.POST, request.FILES, instance=shop_profile)
        if form.is_valid():
            form.save()
            return redirect('shop_profile_detail', pk=shop_profile.pk)
        return render(request, 'shop_profile_details.html', {'form': form})

class ShopHomeView(View):
    def get(self, request, *args, **kwargs):
        try:
            profile = ShopProfileModel.objects.get(shop=request.user.shopuser)
            return render(request, 'shophome.html',{'profile': profile})
        except ShopProfileModel.DoesNotExist:
            return redirect('shop_profile_create') 

class CategoryCreateView(CreateView):
    model = CategoryModel
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryListView(ListView):
    model = CategoryModel
    template_name = 'category_list.html'
    context_object_name = 'categories'

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review_detail.html'
    context_object_name = 'review'
