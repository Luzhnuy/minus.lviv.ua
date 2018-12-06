from django.contrib.auth.models import User
from django import forms
import datetime
from shop.models import BlurbsBlurb,BlurbsBlurbcategory




class BlurbForm(forms.ModelForm):

    class Meta:
        model = BlurbsBlurb
        fields = ['title','description','buysell']

    def save(self,commit=True):
        blurb = super(BlurbForm,self).save(commit=False)
        blurb.pub_date = datetime.datetime.now()
        if commit:
            blurb.save()
        return blurb

class BlurbCategoryForm(forms.ModelForm):

    class Meta:
        model = BlurbsBlurbcategory
        fields = ['title']
