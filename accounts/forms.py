from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

# User 모델이 필요하므로 미리 선언
User = get_user_model()


class UserLoginForm(AuthenticationForm):
    # AuthenticationForm은 request가 인자로 들어가므로 같이 추가해주어야 한다.
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        update_fields = ['username', 'password']
        for field_name in update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })


class UserCreationModelForm(UserCreationForm):
    '''
    __init__(self, *args, **kwargs)
    UserCreationsModel을 상속하며 생성자 새로 정의
    생성자에서 update할 field마다 css 속성 적용
    Meta 클래스에서 fields 선언
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # update할 fileds에 접근하기 위한 임시 이름 지정
        update_fields = ['username', 'password1', 'password2',]
        for field_name in update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]