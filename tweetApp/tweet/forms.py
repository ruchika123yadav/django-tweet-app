from django import forms
from .models import tweet

class tweetForm(forms.ModelForm):
    # class Meta:ye meta class hamesha banani hi padtaa hai
        model=tweet
        fields=['text','photo'];  # ye model wale hi likhe hai text or photo