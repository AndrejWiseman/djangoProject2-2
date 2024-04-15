# from django import forms
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#
#
#
# class myUserCreationForm(UserCreationForm):
#
#     password1 = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )
#     password2 = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )
#
#     class Meta:
#         model = UserCreationForm
#         fields = ('username', 'password1', 'password2')
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             # 'password': TextInput(attrs={'class': 'form-control'}),   # Remove This Line
#             # 'password2': TextInput(attrs={'class': 'form-control'}),  # Remove This Line
#         }