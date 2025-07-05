from django.core.exceptions import ValidationError
from django.db.models import TextField
from django.forms import NumberInput, DateField, ModelForm, CharField, TimeField
from django.forms.widgets import Textarea

from viewer.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['owner_of_event']

        labels = {
            'name': 'Název události',
            'description': 'Popis události',
            'event_image': 'Obrázek',
            'end_time': 'Čas konce',
            'location': 'Lokace',
        }

    start_time = TimeField(
        required=True,
        widget=NumberInput(attrs={'type': 'time'}),
        label='Čas zahájení'
    )

    end_time = TimeField(
        required=True,
        widget=NumberInput(attrs={'type': 'time'}),
        label='Čas ukončení'
    )

    start_date = DateField(
        required=True,
        widget=NumberInput(attrs={'type': 'date'}),
        label='Začátek události'
    )

    end_date = DateField(
        required=True,
        widget=NumberInput(attrs={'type': 'date'}),
        label='Konec události'
    )

    description = CharField(
        required=True,
        min_length=20,
        label='Popis události',
        widget=Textarea(attrs={
            'rows': 5,
            'cols': 50,
        })
    )

    def clean_description(self):
        description_text = self.cleaned_data['description']
        if len(description_text.strip()) < 20:
            raise ValidationError('Popis musí mít alespoň 20 znaků!')
        return description_text

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_date and end_date and end_date < start_date:
            raise ValidationError('Datum konce musí být po datu začátku!')

        if start_date and end_date and start_date == end_date:
            if start_time and end_time and end_time <= start_time:
                raise ValidationError('Čas konce musí být později než čas začátku, pokud je událost v jeden den!')

        return cleaned_data