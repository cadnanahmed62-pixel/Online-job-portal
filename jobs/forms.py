
from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'category',
            'title',
            'description',
            'requirements',
            'location',
            'salary',
        ]

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if len(title) < 3:
            raise forms.ValidationError('Job title must be at least 3 characters long.')
        return title

    def clean_description(self):
        description = self.cleaned_data['description'].strip()
        if len(description) < 20:
            raise forms.ValidationError('Description must be at least 20 characters long.')
        return description

    def clean_location(self):
        location = self.cleaned_data['location'].strip()
        if not location:
            raise forms.ValidationError('Location is required.')
        return location
