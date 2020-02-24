from django import forms
from .models import MakerProfile,BuyerProfile,MstLang,MstSkill,Contact,Order,OrderMessage
from register.models import User





class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('last_name', 'first_name')

class MakerProfileForm(forms.ModelForm):

    class Meta:
        model = MakerProfile
        fields = ('picture', 'lang','cost','skill')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lang'].widget = forms.CheckboxSelectMultiple()
        self.fields['lang'].queryset = MstLang.objects
        self.fields['skill'].widget = forms.CheckboxSelectMultiple()
        self.fields['skill'].queryset = MstSkill.objects



class BuyerProfileForm(forms.ModelForm):

    class Meta:
        model = BuyerProfile
        fields = ('picture',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('user','email','message','file',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({
            'class': 'form-control required',
            'placeholder':'Your Name',
            'data-placement':'top',
            'data-trigger':'manual',
            'data-content':'Must be at least 3 characters long, and must only contain letters.'})
        self.fields['email'].widget.attrs.update({
            'class':'form-control email',
            'placeholder':'email@xxx.com',
            'data-placement':'top',
            'data-trigger':'manual',
            'data-content':'Must be a valid e-mail address (user@gmail.com)',
        })
        self.fields['message'].widget.attrs.update({
            'class':'form-control',
            'placeholder':"Your message here..",
            'data-placement':'top',
            'data-trigger':'manual',
        })

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('title','body','order_type','order_finish_time','cost',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class':'form-control',
            'placeholder':"タイトルを入れてください",
            'data-placement':'top',
            'data-trigger':'manual',
            "data-content" :"依頼の内容入力",
        })
        self.fields['order_type'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['body'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['cost'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['order_finish_time'].widget.attrs.update({
            'class':'form-control',
        })

