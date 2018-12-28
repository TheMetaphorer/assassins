from django import forms


class RegisterForm(forms.Form):
    nick = forms.CharField(label='nickname', max_length=32)

    class Meta:
        classname = 'RegisterForm'
