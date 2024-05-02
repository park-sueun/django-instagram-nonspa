from django.contrib.auth.forms import UserCreationForm
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
            'first_name', 'last_name', 'website_url', 'bio'
        )