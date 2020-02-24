from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email','body','picture')

from .models import MakerProfile,BuyerProfile,MstLang,MstSkill
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


