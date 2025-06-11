from django import forms
from .models import formregister
from django.core.exceptions import ValidationError
class creat_ac(forms.ModelForm):
    confirm_password=forms.CharField(
        widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 bg-gray-700 text-white rounded focus:outline-none focus:ring-2 focus:ring-red-500',
        'placeholder': 'Confirm password'
        }
        )
        
        )
    class Meta:
        model=formregister
        fields=['name','email','password']
        error_messages={
            'name':{'required':"Plese Enter a User name"},
            'email':{'required':"Email is required"},
            'password':{'required':'Password is required for Security'},
            'confirm_password':{'required':'Password is required for Security'}
        }
        widgets={
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 text-white rounded focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 text-white rounded focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Enter your email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 text-white rounded focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Enter your password'
            }),
        }
        labels={
            'name':'Username'
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error(None, "Passwords do not match")
        
        email = cleaned_data.get('email')
        if formregister.objects.filter(email=email).exists():
            self.add_error(None,"This email is already registered. Please use a different one.")
        # return email
     

class forget_pass(forms.Form):
    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'w-full px-4 py-2 bg-gray-700 text-white rounded focus:outline-none focus:ring-2 focus:ring-red-500',}
            
        )
    )  

class change_password(forms.Form):            
    new_password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'w-full px-4 py-2 bg-gray-700 text-white rounded focus:outline-none focus:ring-2 focus:ring-red-500',}
            
        )
    )
    confirm_password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'w-full px-4 py-2 bg-gray-700 text-white rounded focus:outline-none focus:ring-2 focus:ring-red-500',}
            
        )
    )