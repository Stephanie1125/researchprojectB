from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Wrong password.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    confirm_email = forms.EmailField(label='Comfirm email')
    password = forms.CharField(widget=forms.PasswordInput)

    access_code = forms.CharField(label='Sakai Lab access code')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            "confirm_email",
            'password',
            'access_code',
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('confirm_email')
        access_code = self.cleaned_data.get('access_code')

        if email != email2:
            raise forms.ValidationError("Emails must match")

        if access_code != '1984':
            raise forms.ValidationError("Wrong access code. Cannot register.")

        return super(UserRegisterForm, self).clean(*args, **kwargs)

