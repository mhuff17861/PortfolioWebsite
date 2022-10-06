from django import forms

class ContactForm(forms.Form):
    """
    This class defines the form that will be filled out to contact the website owner
    via email
    """
    name = forms.CharField(label='Your name', max_length=100)
    """Variable which holds the name of the message sender"""
    pronouns = forms.CharField(label='Pronouns (optional)', max_length=100, required=False)
    """Variable which holds the message sender's pronouns (optional)"""
    email = forms.EmailField(label='Email', max_length=150)
    """Variable which holds the sender's email address"""
    reason_for_contact = forms.CharField(label='Reason for contacting me', max_length=50)
    """Variable which holds the sender's reason for contact"""
    message = forms.CharField(label='Message', max_length=1000, widget=forms.Textarea)
    """Variable which holds the sender's actual message"""


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
