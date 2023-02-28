from django import forms  
from employee.models import Employee

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    email=forms.EmailField()
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee
        fields = "__all__"
        