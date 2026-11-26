
from django import forms
from .models import JobSeekerProfile


class JobSeekerProfileForm(forms.ModelForm):

    class Meta:
        model = JobSeekerProfile
        fields = [
            'phone_number',
            'address',
            'skills',
            'education',
            'experience',
            'cv',
        ]

        widgets = {
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Enter your address'
            }),
            'skills': forms.Textarea(attrs={
                'placeholder': 'Enter your skills',
                'rows': 3
            }),
            'education': forms.Textarea(attrs={
                'placeholder': 'Enter your education',
                'rows': 3
            }),
            'experience': forms.Textarea(attrs={
                'placeholder': 'Enter your work experience',
                'rows': 3
            }),
        }
