from django import forms
from cartograph.models import Raid


class RaidModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'reportee' in kwargs:
            self.reportee = kwargs.pop('reportee')
            self.reported_by = self.reportee.affiliations.first().organization
        super(RaidModelForm, self).__init__(*args, **kwargs)
        not_required = [
            'city',
            'zip_code',
            'date',
            'time',
            'detainee_count',
            'notes',
            'reportee',
            'reported_by',
            ]
        for field in not_required:
            self.fields[field].required = False
        self.fields['reportee'].initial = self.reportee
        self.fields['reported_by'].initial = self.reported_by

    time = forms.TimeField(
        input_formats=['%H:%M:%S', '%I:%M %p'],
        widget=forms.TextInput(attrs={
            'class': 'gui-input time-picker',
            'placeholder': 'Time'
        }))

    class Meta:
        model = Raid
        fields = [
            'state',
            'city',
            'zip_code',
            'date',
            'time',
            'detainee_count',
            'notes',
            'reportee',
            'reported_by'
        ]
        widgets = {
            'state': forms.Select(attrs={
                'class': 'gui-input',
                'placeholder': 'State',
                }),
            'city': forms.TextInput(attrs={
                'class': 'gui-input',
                'placeholder': 'City',
                }),
            'zip_code': forms.TextInput(attrs={
                'class': 'gui-input',
                'placeholder': 'Zip Code',
                }),
            'date': forms.DateInput(attrs={
                'class': 'gui-input date-picker',
                'placeholder': 'Date',
                }, format='%d/%m/%Y'),
            'detainee_count': forms.TextInput(attrs={
                'class': 'gui-input',
                'placeholder': 'Detainee Count',
                'type': 'number',
                'min': 0
                }),
            'notes': forms.Textarea(attrs={
                'class': 'gui-textarea',
                'placeholder': 'Notes (5000 char limit)',
                'rows': 5
                }),
            'reportee': forms.TextInput(attrs={'class': 'hidden'}),
            'reported_by': forms.TextInput(attrs={'class': 'hidden'}),
        }

    def save(self, *args, **kwargs):
        self.reportee.user
        self.reported_by
        super(RaidModelForm, self).save(*args, **kwargs)
