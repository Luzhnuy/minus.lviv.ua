from minusstore.models import  MinusstoreMinusrecord
from django.contrib.auth.models import User
from django import forms
from mutagen.mp3 import MP3
import datetime



class AddMinusForm(forms.ModelForm):
	# plusrecord = forms.FileField()

	class Meta:
		model = MinusstoreMinusrecord
		# fields = ['title']
		fields = ['file','title','author','lyrics','plusrecord','embed_video']

	

	def save(self,commit=True):
		minus = super(AddMinusForm, self).save(commit=False)
		f = MP3(self.cleaned_data['file'])
		self.bitrate = f.info.bitrate/1000
		self.length = f.info.length
		self.pub_date = datetime.datetime.now()
		if commit:
			minus.save()
		return minus
