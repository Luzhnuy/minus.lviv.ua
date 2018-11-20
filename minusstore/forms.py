from minusstore.models import  MinusstoreMinusrecord
from django import forms

class AddMinusForm(forms.ModelForm):
	class Meta:
		model = MinusstoreMinusrecord
		exclude = ('user_id','files','plusrecord')
