from django import forms

# old school max length
class TweetForm(forms.Form):
    tweet = forms.CharField(widget=forms.Textarea, max_length=140)
