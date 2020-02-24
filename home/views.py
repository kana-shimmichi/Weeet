from django.shortcuts import render,redirect
from django.views import generic


from .forms import UserForm,MakerProfileForm,BuyerProfileForm,ContactForm,OrderForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


##model
from .models import MakerProfile,Like,BuyerProfile,Contact,Order,MstStatus,Like
from .models import Order as OrderModel
from register.models import UserRole

import datetime


##COMPLETE##
class Top(generic.TemplateView):
    template_name = 'home/Top.html'

class About(generic.TemplateView):
    template_name = 'home/about.html'


class Contact(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "home/contact.html"
    success_url = "/"  # 成功時にリダイレクトするURL

class Diagnosis(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/diagnosis.html'


class Instructions(generic.TemplateView):
    template_name = 'home/instractions.html'

class Question(generic.TemplateView):
    template_name = 'home/question.html'


class Order_Job(generic.CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'home/order_job.html'
    success_url = "/"  # 成功時にリダイレクトするURL
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        status=MstStatus.objects.get(id=1)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.buyer= request.user
            obj.order_post=True
            obj.order_post_at=datetime.datetime.now()
            obj.status=status
            obj.save()
        return redirect('/')


class ResearchResult(generic.ListView):
    model = Order
    template_name = "home/research_result.html"
    paginate_by = 10


def order_detail(request,order_id):
    return render(request,'home/order_detail.html')

def like(request,order_id):

    like_order = OrderModel.objects.get(id=order_id)
    like,_ = Like.objects.get_or_create(user=request.user,like_order=like_order)
    like.save()

    return redirect('/')

def submit(request,order_id):
    return redirect('/')








##COMPLETE##
class RoleChoice(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/menu/role_choice.html'

def addRole(request):
    user=request.user
    user_role=UserRole.objects.get(id=int(request.POST["role"]))
    user.user_role=user_role
    user.save()
    user_forms=UserForm()
    if user_role.id==1:
        profile_forms=MakerProfileForm()
    else:
        profile_forms=BuyerProfileForm()
    data={
        "user_forms":user_forms,
        "profile_forms":profile_forms
    }
    return render(request,'home/menu/profile_edit.html',data)


def addProfile(request):
    user=request.user
    user.first_name=request.POST["first_name"]
    user.last_name=request.POST["last_name"]
    user.save()
    if user.user_role.id==1:
        profile_forms = MakerProfileForm(request.POST,request.FILES)
    else:
        profile_forms = BuyerProfileForm(request.POST,request.FILES)
    if profile_forms.is_valid():
        profile=profile_forms.save(commit=False)
        profile.user=request.user
        profile.save()
        return redirect("/my_menu/")



def change_profile(request):
    user=request.user
    user_forms=UserForm(instance=user)
    if user.user_role.id==1:
        profile=MakerProfile.objects.get(user=user)
        profile_forms=MakerProfileForm(instance=profile)

    else:
        profile = BuyerProfile.objects.get(instance=profile)
        profile_forms=BuyerProfileForm()


    data={
        "user_forms":user_forms,
        "profile_forms":profile_forms
    }
    return render(request,'home/menu/profile_edit.html',data)


















