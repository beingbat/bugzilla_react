from random import choices
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

    name = forms.CharField(max_length=50)
    description = forms.TextInput()

    class Meta:
        model = Project
        fields = ('name', 'description',)



class ProjectChooseForm(forms.ModelForm):
    projects_field = forms.ChoiceField(choices=())

    class Meta:
        model = Project
        fields = ('projects_field', )

    def __init__(self, *args, **kwargs):
        super(ProjectChooseForm, self).__init__(*args, **kwargs)
        self.fields['projects_field'] = forms.ChoiceField(choices=self.get_choices())

    def get_choices(self):

        projects = Project.objects.all()
        choices = ((-1, 'None'), )
        for project in projects:
            choices = choices + ((project.id, project.name),)
        return choices
