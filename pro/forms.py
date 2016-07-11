__author__ = 'venut'


from django import forms
from .models import Projectstatus, Shot, Assosiate
from django.contrib.auth.models import User

class registrationForm(forms.ModelForm):
    username=forms.CharField(label=u"username")
    email = forms.EmailField(label=u'email')
    password=forms.CharField(label=u'password',widget = forms.PasswordInput(render_value=False))
    password1=forms.CharField(label=u'verify password',widget = forms.PasswordInput(render_value=False))

    class Meta:
        model=Assosiate
        exclude=('user','group')

    def clean_username(self):
        username=self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('User name already taken. try another')


class loginForm(forms.Form):
    username=forms.CharField(label=u"username")
    password=forms.CharField(label=u'password',widget = forms.PasswordInput(render_value=False))


class resetForm(forms.Form):
    password=forms.CharField(label=u'password',widget = forms.PasswordInput(render_value=False))
    password1=forms.CharField(label=u'password1',widget = forms.PasswordInput(render_value=False))
    password2=forms.CharField(label=u'password2',widget = forms.PasswordInput(render_value=False))

class ProjectstatusForm(forms.ModelForm):
    class Meta:
        model = Projectstatus
        fields = ['project','seq','shot','dept','statuscode']

    # def __init__(self, *args, **kwargs):
    #     super(ProjectstatusForm, self).__init__(*args, **kwargs)
    #     self.fields['statuscode'].queryset = StatusCodes.objects.filter(department_id=self.instance.department.id)  ## self.instance.department.id


class ShotForm(forms.ModelForm):
    class Meta:
        model = Shot
        fields = "__all__"