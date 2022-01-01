from django import forms

from .models import JobPost

class NewJob(forms.ModelForm):

    class Meta:
        model = JobPost
        fields = ('job_title','job_detail', 'job_price', 'job_creator')