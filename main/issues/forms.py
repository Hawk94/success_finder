from django.forms import ModelForm
from .models import Issue


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['type', 'priority', 'category']