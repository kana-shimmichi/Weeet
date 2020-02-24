
from django.shortcuts import render,redirect

from django.views import generic
from .models import Contact
from .forms import ContactForm



from .forms import UserForm,MakerProfileForm,BuyerProfileForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


##model
from .models import MakerProfile,Like,BuyerProfile
from .models import Order as OrderModel


from register.models import UserRole


##COMPLETE##

class Top(generic.TemplateView):
    template_name = 'home/top.html'
##about
class About(generic.TemplateView):
    template_name = 'home/about.html'

##question
class Question(generic.TemplateView):
    template_name = 'home/question.html'


class Menu(generic.TemplateView):
    template_name = 'home/menu.html'



class About(generic.TemplateView):
    template_name = 'home/about.html'


class Instructions(generic.TemplateView):
    template_name = 'home/instractions.html'



class Contact(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "home/contact.html"
    success_url = "/"  # 成功時にリダイレクトするURL



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
        profile_forms = MakerProfileForm(request.POST)
    else:
        profile_forms = BuyerProfileForm(request.POST)

    if profile_forms.is_valid():
        profile=profile_forms.save(commit=False)
        profile.user=request.user
        profile.save()

    return redirect("/menu/")



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


@login_required
def menu(request):
    user=request.user
    if not user.user_role:
        return redirect("/choice_role")

    role=user.user_role
    if role.id==1:##作成者
        profile =MakerProfile.objects.get(user=user)
        orders = OrderModel.objects.filter(maker_decided=user)

    else:
        profile = BuyerProfile.objects.get(user=user)
        orders = OrderModel.objects.filter(buyer=user)

    likes=Like.objects.filter(user=user)


    data={
        "profile":profile,
        "likes":likes,
        "orders":orders,
    }
    return render(request,'home/menu.html',data)








class Diagnosis(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/diagnosis.html'


class OrderSubmit(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/order/order.html'


class Request(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/order/order_edit.html'

@login_required
def addLike(request,id):
    return redirect('/orders')

class Contacts(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/order/order.html'


class OrdersList(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/index.html'

class Makers(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/index.html'

class MakersEdit(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/order/makers_edit.html'

class Message(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/index.html'

class MessageDetail(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/index.html'

class Order(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/index.html'

class OrderReply(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/index.html'

class OrderPay(generic.TemplateView,LoginRequiredMixin):
    template_name = 'home/index.html'
