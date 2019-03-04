from django import forms
from .models import Blog

# models.py 에 있는 클래스를 기반으로 하기 때문에 ModelForm
class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
        fields = ['title', 'body']

# class BlogPost(forms.Form):
#     email = forms.EmialField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length=200)
#     max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])

    # 다중선택가능한 입력공간
    