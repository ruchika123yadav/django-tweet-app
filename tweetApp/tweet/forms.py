from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta: #ye meta class hamesha banani hi padti hai
        model=Tweet #model konsa use kr rhe ho or field kitne use krna chahte ho
        fields=['text','photo'];  # ye model wale hi likhe hai text or photo


