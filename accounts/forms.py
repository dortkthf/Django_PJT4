from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):

   class Meta(UserCreationForm.Meta): 
        model = get_user_model()
        fields = ('username','email','password1','password2')
        labels = {
            'username':'닉네임',
            'email' : '이메일',
            'password1': '비밀번호',
            'password2' : '비밀번호 확인'
        }




