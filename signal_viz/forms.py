from django import forms


class excel_upload_form(forms.Form):
    uploaded_file = forms.FileField()
    uploaded_file.label = ''
    # nr_report.label.widget.attrs.update({'class':'form-control'})
    uploaded_file.widget.attrs.update({'class':'form-control'})