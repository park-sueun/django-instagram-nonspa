from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordChangeForm as AuthPasswordChangeForm
)
from django.forms import ValidationError, ModelForm
from .models import User

class SignupForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name'
        )
        
    def clean_email(self):
        """Reject usernames that differ only in case."""
        email = self.cleaned_data.get("email")
        if email:
            queryset = User.objects.filter(email=email)
            if queryset.exists():
                raise ValidationError("이미 등록된 이메일 주소입니다.")
        
        return email
    
class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'profile', 'first_name', 'last_name', 'gender', 'phone_number', 'website_url', 'bio'
        )
        
class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        
        if old_password == new_password1:
            raise ValidationError("새로운 암호는 기존 암호와 다르게 입력해주세요.")
        
        return new_password1