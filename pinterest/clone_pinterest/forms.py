from django import forms
from .models import Board,Pin,Profile,Comments,SavedPin

class BoardForm(forms.ModelForm):
    
    class Meta:
        model=Board
        exclude=['user']



class PinForm(forms.ModelForm):
    
    class Meta:
        model=Pin
        exclude=['user']



class ProfileForm(forms.ModelForm):
    
    class Meta:
        model=Profile
        # fields="__all__"
        exclude=['user']


class CommentsForm(forms.ModelForm):
    
    class Meta:
        model=Comments
        fields=['comment']


class SavedPinForm(forms.ModelForm):
    
    class Meta:
        model=SavedPin
        fields=['board']