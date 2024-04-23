from django.forms import ModelForm
from .models import Bb

class BbForm(ModelForm): # стр 61
	class Meta:
		model = Bb
		fields = ('title', 'content', 'price', 'rubric')
