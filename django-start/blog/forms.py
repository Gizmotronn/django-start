from django import forms # forms class from django module/libary

class CommentForm(forms.Form): # create a new class, displaying the comments form and inheriting from the django forms class
    author = forms.CharField( # similar to a field/model. Name of the field - author of type char field
        max_length=60, 
        widget=forms.TextInput(attrs={ # text widgets
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control", # the comment
            "placeholder": "Leave a comment!"
        })
    )