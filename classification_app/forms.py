from django import forms

class upload_image_form(forms.Form):
    #SYMPTOMS = forms.ChoiceField(required=False,choices = symptons,widget=forms.CheckboxSelectMultiple)
    # symp1 = forms.BooleanField(required=False, label='Fever')
    # symp2 = forms.BooleanField(required=False, label='Dry Cough')
    # symp3 = forms.BooleanField(required=False, label='Tiredness')
    # symp4 = forms.BooleanField(required=False, label='Aches and Pains')
    # symp5 = forms.BooleanField(required=False, label='Sore Throat')
    # symp6 = forms.BooleanField(required=False, label='Diarrhoea')
    # symp7 = forms.BooleanField(required=False, label='Conjunctivitis')
    # symp8 = forms.BooleanField(required=False, label='Headache')
    # symp9 = forms.BooleanField(required=False, label='Loss of Taste or Smell')
    # symp10 = forms.BooleanField(required=False, label='Difficulty Breathing or Shortness of Breath')
    # symp11 = forms.BooleanField(required=False, label='Chest Pain or Pressure')
    # symp12 = forms.BooleanField(required=False, label='Loss of Speech or Movement')

    Image = forms.ImageField()
