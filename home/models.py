from django.db import models
from register.models import User
# Create your models here.


class Contact(models.Model):
    class Meta:
        verbose_name_plural="コンタクト"
    name = models.CharField("お名前",max_length=30)
    email = models.EmailField("メールアドレス")
    body = models.TextField("問い合わせ")
    picture = models.FileField("添付ファイル")
    def __str__(self):
        return self.name



class MstLang(models.Model):
    class Meta:
        verbose_name_plural="M_言語"
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class MstCost(models.Model):
    class Meta:
        verbose_name_plural="M_コスト"
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class MstSkill(models.Model):
    class Meta:
        verbose_name_plural="M_スキル"
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class CreditInfomation(models.Model):
    class Meta:
        verbose_name_plural="クレジット情報"
    name=models.CharField(max_length=10)
    credit_infomation = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class BuyerProfile(models.Model):
    class Meta:
        verbose_name_plural="購入者プロフィール"
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField(blank=True,null=True)
    estimate_point=models.FloatField(default=0)
    credit_customer=models.CharField(max_length=50,blank=True)
    credit_info=models.ManyToManyField(CreditInfomation,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





class MakerProfile(models.Model):
    class Meta:
        verbose_name_plural="作成者プロフィール"
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField(blank=True,null=True)
    lang = models.ManyToManyField(MstLang)
    cost = models.ForeignKey(MstCost,on_delete=models.CASCADE,blank=True,null=True)
    skill = models.ManyToManyField(MstSkill)

    estimate_point=models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Order(models.Model):
    class Meta:
        verbose_name_plural="オーダー"

    buyer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Buyer")
    STATUS_CHOICES = ((0, '普通'), (1, '普通じゃない'))

    title = models.CharField("タイトル",max_length=20)
    body = models.TextField("発注詳細")
    order_finish_time = models.DateTimeField("納品希望日",blank=True,null=True)



    cost = models.IntegerField("金額の目安")

    order_post=models.BooleanField(default=False)
    order_post_finish_time = models.DateTimeField(blank=True,null=True)
    order_post_at = models.DateTimeField(blank=True,null=True)
    order_decide = models.BooleanField(default=False)
    order_decide_at = models.DateTimeField(blank=True,null=True)

    makers = models.ManyToManyField(User,blank=True)

    maker_decided = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Maker_decided",blank=True,null=True)

    order_confirm = models.BooleanField(default=False)
    order_confirm_at = models.DateTimeField(blank=True,null=True)

    order_pay = models.BooleanField(default=False)
    order_pay_at = models.DateTimeField(blank=True,null=True)

    order_finish = models.BooleanField(default=False)
    order_finish_at = models.DateTimeField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderMessage(models.Model):
    class Meta:
        verbose_name_plural="オーダーメッセージ"
    buyer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="MessageBuyer")
    maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="MessageMaker")
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True)
    body= models.TextField()
    file = models.FileField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

class Like(models.Model):
    class Meta:
        verbose_name_plural="favorite"
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")
    del_flg=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
