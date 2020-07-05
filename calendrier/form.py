
from django.forms import ModelForm, DateInput
from .models import maintenance

class EventForm(ModelForm):
  class Meta:
    model = maintenance
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['date'].input_formats = ('%Y-%m-%dT%H:%M',)
    