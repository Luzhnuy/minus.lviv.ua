from minusstore.models import  MinusstoreMinusrecord,Minusgenre,Minusappointment
from django.contrib.auth.models import User
from django import forms
from mutagen.mp3 import MP3
import datetime



class AddMinusForm(forms.ModelForm):
	# plusrecord = forms.FileField()
    class Meta:
        model = MinusstoreMinusrecord
        # fields = ['title']
        fields = ['file','author','title','lyrics','plusrecord','embed_video',]

    def save(self,commit=True):
        minus = super(AddMinusForm, self).save(commit=False)
        f = MP3(self.cleaned_data['file'])
        self.title = self.cleaned_data['title']
        self.bitrate = f.info.bitrate/1000
        self.length = f.info.length
        self.pub_date = datetime.datetime.now()
        minus_genre = Minusgenre.objects.get(name=self.cleaned_data['genre'])
        self.minus_genre = minus_genre
        minus_appointment = Minusappointment.objects.get(name=self.cleaned_data['specifik'])
        self.minus_appointment = minus_appointment
        if commit:
            minus.save()
        return minus
