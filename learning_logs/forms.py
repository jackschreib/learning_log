from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'hours_spent', 'study_date']
        labels = {'text': 'Entry Text', 'hours_spent': 'Hours Spent', 'study_date': 'Study Date',}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

 
