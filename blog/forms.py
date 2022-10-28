from django import forms


class CommentForm(forms.Form):
    text = form.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment..."
        }
    ))
    author = form.CharField(max_lenght=64, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Enter your name..."
        }
    ))