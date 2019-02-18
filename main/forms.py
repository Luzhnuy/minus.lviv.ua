from django import forms
# from user.models import AuthUser
from django.contrib.auth.models import User
from main.models import NewsNewsitem

class AuthForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password', )




class AddNews(forms.ModelForm):

	class Meta:
		model = NewsNewsitem
		fields = ('title','preview','body')


# class RegisterFormView(FormView):
#     form_class = UserCreationForm

#     # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
#     # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
#     success_url = "http://127.0.0.1:8000"

#     # Шаблон, который будет использоваться при отображении представления.
#     template_name = "user/registration.html"

#     def form_valid(self, form):
#         # Создаём пользователя, если данные в форму были введены корректно.
#         form.save()

#         # Вызываем метод базового класса
#         return super(RegisterFormView, self).form_valid(form)
