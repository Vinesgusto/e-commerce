from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['foto']
        widgets = {
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}), # Adiciona classe Bootstrap ao input de arquivo
        }