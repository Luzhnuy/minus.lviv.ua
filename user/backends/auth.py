# from django.conf import settings
# from django.contrib.auth.models import User
# import datetime
# from django.contrib.auth.forms import AuthenticationForm
# from django.http import HttpResponse,HttpResponseRedirect
#
#
# class EmailOrUsernameModelBackend(AuthenticationForm):
#     """
#     Implements an authorization with email instead of login
#     """
#
#     def authenticate(self, username=None, password=None):
#         if '@' in username:
#             kwargs = {'email': username}
#         else:
#             kwargs = {'username': username}
#         try:
#             user = User.objects.get(**kwargs)
#             print('hell')
#             if user.check_password(password):
#                 if user.get_profile().banned:
#                     profile = user.get_profile()
#                     if datetime.date.today() < profile.banned_until:
#                         return None
#                         print('hell2')
#                     else:
#                         print('hell3')
#                         profile.banned = False
#                         profile.save()
#                         return user
#                 else:
#
#                     return HttpResponseRedirect('../../')
#         except User.DoesNotExist:
#             print('hell1')
#             return None
