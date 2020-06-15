from django import forms
from django import template

RANK_CHOICES = (
    ('nothing', 'Please choose'),
    ('dev', 'Developer'),
    ('mod', 'Moderator'),
    ('builder' ,'Builder'),
    ('helper', 'Helper'),
)

AGE_CHOICES = (
    ('12', 'Below 12'),
    ('12+', '12-14'),
    ('14+','14-16'),
    ('18', '18+'),
)

TIME_SPEND_CHOICES = (
    ('1', 'Less than a week'),
    ('2', '1-4 weeks'),
    ('3', '1-3 months'),
    ('4', '3-6 months'),
    ('5', '6-9 months'),
    ('6', '9-12 months'),
    ('7', 'More than a year'),
)

KIND_DEV_CHOICES = (
    ('fullstack', 'full stack web developer (Python Django)'),
    ('frontend', 'frontend web developer (Any frontend framework that works with Python Django)'),
    ('backend', 'backend web developer (Python Django)'),
    ('mg', 'minigame plugins developer (Java)'),
    ('moderation', 'moderation plugins developer (Java)'),
    ('cosmetic', 'cosmetic plugins developer (Java)'),
)

class ContactUsForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input1'}))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input1'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input1'}))
    msg = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'input1'})
    )

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name"
        self.fields['contact_email'].label = "Your email"
        self.fields['subject'].label = "Subject"
        self.fields['msg'].label = "Your issue"


class ApplyForStaffForm(forms.Form):
    # Base
    rank_choices = forms.ChoiceField(required=True, choices=RANK_CHOICES, widget=forms.Select(attrs={'class': 'selection-2'}))
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input100'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input100'}))
    ign = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input100'}))
    age = forms.ChoiceField(required=True, choices=AGE_CHOICES, widget=forms.Select(attrs={'class': 'selection-2'}))
    timezone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input100'}))
    time_spend = forms.ChoiceField(required=True, choices=TIME_SPEND_CHOICES, widget=forms.Select(attrs={'class': 'selection-2'}))
    why_do_u_want_to_be_staff = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'input100'}))
    why_us = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'input100'}))

    # Dev Rank
    dev_kind_of_dev = forms.ChoiceField(required=True, choices=KIND_DEV_CHOICES, widget=forms.Select(attrs={'class': 'selection-2'}))
    dev_creations = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input100'}))

    # Moderator Rank
    mod_how_will_deal_with_a_case = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'input100'}))
    mod_previous_experiences = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'input100'}))

    # Helper Rank
    helper_how_will_deal_with_a_case = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'input100'}))
    helper_previous_experiences = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'input100'}))

    # Builder Rank
    builder_previous_build_experiences = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'input100'}))
    builder_one_of_best_builds = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'input100'}))

