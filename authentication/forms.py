from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(max_length=50, label="Nom d'utilisateur :")
    password = forms.CharField(min_length=8, max_length=20,
                               widget=forms.PasswordInput, label="Mot de passe :")
    password_confirm = forms.CharField(min_length=8, max_length=20,
                                       widget=forms.PasswordInput, label="Confirmer mdp :")
