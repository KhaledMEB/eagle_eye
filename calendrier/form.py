
from django.forms import ModelForm, DateInput, forms
from .models import maintenance
import datetime

class EventForm(ModelForm):
  class Meta:
    model = maintenance
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    
    fields = ['titre','date','voiture','employee','etat','description']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['date'].input_formats = ('%Y-%m-%dT%H:%M',)
  def valide_date(date):
        
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date