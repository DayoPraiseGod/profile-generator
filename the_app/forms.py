from django.db.models import fields
from django.forms import ModelForm
from .models import Portfolio


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
        exclude = ['project', 'project_title', 'project_description']