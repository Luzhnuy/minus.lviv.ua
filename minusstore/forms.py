from minusstore.models import  MinusstoreMinusrecord
from django import forms

class AddMinusForm(forms.ModelForm):
	plusrecord = forms.FileField()

	class Meta:
		model = MinusstoreMinusrecord
		fields = ['title','author','file','lyrics','bitrate','user','length','embed_video']
