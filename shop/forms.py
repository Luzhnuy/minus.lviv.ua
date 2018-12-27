from django.contrib.auth.models import User
from django import forms
from shop.models import BlurbsBlurb,BlurbsBlurbcategory




class BlurbForm(forms.ModelForm):

    class Meta:
        model = BlurbsBlurb
        # fields = "__all__"
        fields = ['title','buysell','description','category','georegion']

    # def save(self,commit=True):
    #     blurb = super(BlurbForm,self).save(commit=False)
    #     if commit:
    #         blurb.save()
    #     return blurb
