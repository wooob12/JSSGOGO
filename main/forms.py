from django import forms
from .models import Jasoseol, Comment

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class': 'jsstitle',
            'placeholder' : '제목',
        })
        self.fields['content'].widget.attrs.update({
            'class': 'jss_content_form',
        })

        


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )