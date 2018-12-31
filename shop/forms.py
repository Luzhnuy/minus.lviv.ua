from django.contrib.auth.models import User
from minus.models import PhotosPhotoalbum,PhotosPhoto
from django import forms
from shop.models import BlurbsBlurb,BlurbsBlurbcategory




class BlurbForm(forms.ModelForm):
    first_photo = forms.FileField()
    second_photo = forms.FileField()
    third_photo = forms.FileField()

    class Meta:
        model = BlurbsBlurb
        # fields = "__all__"
        fields = ['title','cost','buysell','description','category','georegion']

    def save(self,commit=True):
        blurb = super(BlurbForm,self).save(commit=False)
        photo_album = PhotosPhotoalbum.objects.create(user=blurb.user,name = blurb.title,slug="http://minus.lviv.ua/shop/",size = 3,content_type_id=18,object_pk=BlurbsBlurb.objects.get().last().id+1)
        photo = PhotosPhoto.objects.create(title= blurb.title,image=blurb.first_photo,album=photo_album,is_cover=0)
        if blurb.second_photo:
            second_photo = PhotosPhoto.objects.create(title= blurb.title,image=blurb.second_photo,album=photo_album,is_cover=0)
        if blurb.third_photo:
            third_photo = PhotosPhoto.objects.create(title= blurb.title,image=blurb.third_photo,album=photo_album,is_cover=0)
        if commit:
            blurb.save()
        return blurb
