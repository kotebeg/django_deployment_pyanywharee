from django import forms


class csv_upload_form(forms.Form):
    nr_report = forms.FileField()
    nr_report.label = ''
    # nr_report.label.widget.attrs.update({'class':'form-control'})
    nr_report.widget.attrs.update({'class':'form-control'})


# class wo_uploads_form(forms.Form):
#     wo_file = forms.FileField()
#     wo_file.label = 'WO'
#     wo_file.widget.attrs.update({'class':'form-control'})