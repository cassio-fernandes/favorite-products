from django import forms
from django.contrib.auth.models import User
from .models import Client


class ClientForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email já cadastrado!")
        return email

    @staticmethod
    def _before_save(args):
        password = args.pop('password')
        user = User(**args)
        user.set_password(password)
        user.save()

        return user

    def save(self, commit=True):
        if self.password != self.confirm_password:
            raise forms.ValidationError("As senhas informadas não são iguais")

        if commit:
            user = self._before_save({
                'first_name': self.cleaned_data["name"],
                'username': self.cleaned_data["email"],
                'email': self.cleaned_data["email"],
                'password': self.cleaned_data["password"]
            })

            client = Client(user=user)
            client.save()

        return client
