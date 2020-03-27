from django.shortcuts import render,redirect
from django.views import generic
from register.models import User
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from home.models import Like,Order,OrderMessage,MakerProfile,BuyerProfile
from home.models import MstStatus as MstStatusModel
from django.db.models import Q
import datetime
import requests

#マイページトップ
# ログインした人だけ見れるよ。

@login_required
def menu(request):
    if request.user.user_role is None:
        return redirect("/role_choice")

    elif request.user.user_role.id==1:
        profile = MakerProfile.objects.get(user=request.user)

        my_orders = Order.objects.filter(
            Q(maker_decided=request.user),
            Q(status=MstStatusModel.objects.get(id=2))|
            Q(status=MstStatusModel.objects.get(id=3)))

        my_fin_orders=Order.objects.filter(
            Q(maker_decided=request.user),
            Q(status=MstStatusModel.objects.get(id=6))|
            Q(status=MstStatusModel.objects.get(id=4))|
            Q(status=MstStatusModel.objects.get(id=5)))

        likes = Like.objects.filter(user=request.user, like_order__status__id=1)

        data={
            'likes':likes,
            'profile':profile,
            'my_orders':my_orders,
            'my_fin_orders':my_fin_orders,

        }
        return render(request,'my_page/my_menu.html',data)


    else:
        profile = BuyerProfile.objects.get(user=request.user)

        my_orders = Order.objects.filter(
            Q(buyer=request.user),
            Q(status=MstStatusModel.objects.get(id=1)))

        my_decided_orders = Order.objects.filter(
            Q(buyer=request.user),
            Q(status=MstStatusModel.objects.get(id=2))|
            Q(status=MstStatusModel.objects.get(id=3))
        )
        my_fin_orders=Order.objects.filter(
            Q(buyer=request.user),
            Q(status=MstStatusModel.objects.get(id=6))|
            Q(status=MstStatusModel.objects.get(id=4))|
            Q(status=MstStatusModel.objects.get(id=5)))

        data={
            'my_decided_orders':my_decided_orders,
            'profile':profile,
            'my_orders':my_orders,
            'my_fin_orders':my_fin_orders,

        }
        return render(request,'my_page/my_menu_for_buyer.html',data)

def submit(request,order_id):
    order=Order.objects.get(id=order_id)
    order.makers.add(request.user)
    return redirect('/my_menu')




def order_decide(request,order_id,customer_id):
    order=Order.objects.get(id=order_id)
    order.status=MstStatusModel.objects.get(id=2)
    user=User.objects.get(id=customer_id)
    order.maker_decided=user
    order.order_confirm=True
    order.order_confirm_at=datetime.datetime.now()
    order.save()
    return redirect('/my_menu')


class Profile(generic.CreateView):
    template_name = 'my_page/profile_.html'


class Register_Info(generic.TemplateView):
    template_name = 'my_page/register_info.html'

class Orderer_Info(generic.TemplateView):
    template_name = 'my_page/orderer_info.html'

class Contractor_Info(generic.TemplateView):
    template_name = 'my_page/contractor_info.html'


def message(request,customer_id):
    if request.method=="POST":
        user = User.objects.get(id=customer_id)
        if request.user.user_role.id==1:
            OrderMessage.objects.create(
                buyer=user,
                maker=request.user,
                talker=request.user,
                body=request.POST["body"],
                file=request.FILES,
            )
        else:
            OrderMessage.objects.create(
                buyer=request.user,
                maker=user,
                talker=request.user,
                body=request.POST["body"],
                file=request.FILES,
            )
    talk_lists = {}
    user = User.objects.get(id=customer_id)
    if request.user.user_role.id==1:
        messages=OrderMessage.objects.filter(maker=request.user,buyer=user).order_by('updated_at')
        message_profile=BuyerProfile.objects.get(user=user)
        msgs = OrderMessage.objects.filter(maker=request.user).order_by('-updated_at')
        for message in msgs:
            profile=BuyerProfile.objects.get(user=message.buyer)
            talk_lists[message.buyer]=[profile,message.updated_at]
    else:
        messages=OrderMessage.objects.filter(buyer=request.user,maker=user).order_by('updated_at')
        message_profile = MakerProfile.objects.get(user=user)
        msgs = OrderMessage.objects.filter(buyer=request.user).order_by('-updated_at')
        for message in msgs:
            profile = MakerProfile.objects.get(user=message.maker)
            talk_lists[message.maker]=[profile,message.updated_at]
    data={
        "messages":messages,
        "talk_lists":talk_lists,
        'message_profile':message_profile,
    }
    return render(request,'my_page/message.html',data)


def complete(request,order_id):
    order=Order.objects.get(id=order_id)
    status=MstStatusModel.objects.get(id=6)
    order.status=status
    order.save()
    return redirect('/my_menu')



def pay(request, order_id):
    order=Order.objects.get(id=order_id)
    if order.order_pay:
        return redirect('/my_menu')
    data={
        'order':order
    }
    return render(request,'my_page/pay.html',data)


def pay_credit(request,order_id):
    if request.method=="POST":

        request_url = "https://api.pay.jp/v1/charges"
        params = {
            "amount": int(request.POST["cost"]),  # テスト用に金額を1000円で設定
            "currency": "jpy",
            "card": request.POST["payjp-token"]  # カードのトークン
        }
        requests.post(request_url, params, auth=('sk_test_b8ed4e1dfbe222ae1b8b8828', ""))
        order=Order.objects.get(id=order_id)
        status=MstStatusModel.objects.get(id=3)
        order.status=status
        order.order_pay=True
        order.order_pay_at=datetime.datetime.now()
        order.save()

    return redirect('/my_menu')


def cancel(request,order_id):
    order=Order.objects.get(id=order_id)
    order.status=MstStatusModel.objects.get(id=5)
    order.save()
    return redirect('/my_menu')

def order_fin(request,order_id):
    order=Order.objects.get(id=order_id)
    order.status=MstStatusModel.objects.get(id=4)
    order.order_finish=True
    order.order_finish_at=datetime.datetime.now()
    order.save()
    return redirect('/my_menu')

#マイページ　表の中
class Favorite_List(generic.TemplateView):
    template_name = 'my_page/favorite_list.html'

class Trade_list(generic.TemplateView):
    template_name = 'my_page/trade_list.html'

class Request_Job(generic.TemplateView):
    template_name = 'my_page/request_job.html'

class Consent_list(generic.TemplateView):
    template_name = 'my_page/consent_list.html'

class Complate_list(generic.TemplateView):
    template_name = 'my_page/complate_list.html'

#マイページ　表の中の機能
class Comfirm(generic.TemplateView):
    template_name = 'my_page/comfirm.html'

class Change(generic.TemplateView):
    template_name = 'my_page/change.html'

class Approval(generic.TemplateView):
    template_name = 'my_page/approval.html'

class Cancel(generic.TemplateView):
    template_name = 'my_page/cancel.html'

class Complate(generic.TemplateView):
    template_name = 'my_page/complate.html'








