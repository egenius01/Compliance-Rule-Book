from django import forms
from .models import MasterRuleBook, Upload


class UploadForm(forms.ModelForm):

    class Meta:
        model = Upload
        fields = ['returns','images','description']
        exclude = ['posted_by']
        
        
class AuthenticateForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['approved']
        exclude = ['posted_by', 'returns','images','description']


# class EditRuleForm(forms.Form):
#     title = forms.CharField()
#     reference_number = forms.CharField()
#     date_of_issuance =forms.DateField()
#     theme = forms.CharField()
#     Description = forms.CharField()
#     Remark = forms.CharField()