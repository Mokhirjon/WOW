from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Customuser


# create new user
class CustomusersCReate(UserCreationForm):
    class Meta(UserCreationForm):
        model = Customuser
        fields = ('username','password','role','phone')

# update user
class CustomusersUpdate(UserChangeForm):

    class Meta(UserChangeForm):
        model = Customuser
        fields = ('username', 'password', 'role', 'phone')
