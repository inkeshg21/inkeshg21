# from django import forms
# from django.contrib.auth.forms import UserCreationForm

# from custom_auth.models import User


# class NewUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "email", "password1", "password2", "role")

#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user
