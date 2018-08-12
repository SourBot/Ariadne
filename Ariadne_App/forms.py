from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=60, widget=forms.TextInput(
    attrs={"class":"form-control", "placeholder": "Enter todo i.e. delete junk files", "aria-label":"Todo", "aria-describedby": "add-btn"}
    ))
