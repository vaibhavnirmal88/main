from django import forms 


class Receipt(forms.Form):
    name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'class':"form-control"}))
    date=forms.DateField()
    email=forms.CharField(label="E-mail",widget=forms.TextInput(attrs={'class':"form-control"}))
    mobile_number=forms.CharField(label="Mobile No.",widget=forms.TextInput(attrs={'class':"form-control"}))
    amount=forms.CharField(label="Amount",widget=forms.TextInput(attrs={'class':"form-control"}))