from django import forms
from .models import Registration_type,Member_type,Applicant_details,Academic_qualification,Specialized_area,Information_on_present_position,Length_of_tenure,Courses_related_to_quality_management,Other_management_system_trainings,Code_of_conduct, Statement_of_the_applicant

class Registration_type_forms(forms.ModelForm):
        class Meta:
            model = Registration_type
            exclude=('user',)

class Member_type_forms(forms.ModelForm):
       class Meta:
           model = Member_type
           exclude = ('user',)

class Applicant_details_forms(forms.ModelForm):
       class Meta:
           model = Applicant_details
           exclude = ('user',)

class Academic_qualification_forms(forms.ModelForm):
      class Meta:
          model = Academic_qualification
          exclude = ('user',)

class Specialized_area_forms(forms.ModelForm):
      class Meta:
          model = Specialized_area
          exclude = ('user',)

class Information_on_present_position_forms(forms.ModelForm):
      class Meta:
          model = Information_on_present_position
          exclude = ('user',)

class Length_of_tenure_forms(forms.ModelForm):
      class Meta:
          model = Length_of_tenure
          exclude = ('user',)

class Courses_related_to_quality_management_forms(forms.ModelForm):
      class Meta:
          model = Courses_related_to_quality_management
          exclude = ('user',)

class Other_management_system_trainings_forms(forms.ModelForm):
      class Meta:
          model = Other_management_system_trainings
          exclude = ('user',)

class Code_of_conduct_forms(forms.ModelForm):
      class Meta:
          model = Code_of_conduct
          exclude = ('user',)

class Statement_of_the_applicant_forms(forms.ModelForm):
      class Meta:
          model = Statement_of_the_applicant
          exclude = ('user',)

