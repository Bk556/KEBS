from django.urls import path
from membership.views import *

app_name = "membership"
urlpatterns = [
    path("regtype", Registration_type_view, name="regtype"),
    path("membertype", Member_type_view, name="membertype"),
    path("applicant_details", Applicant_details_view, name="applicant_details"),
    path("academic_qualification", Academic_qualification_view, name="academic_qualification"),
    path("specialized_area", Specialized_area_view, name="specialized_area"),
    path("information_on_present_position", Information_on_present_position_view, name="information_on_present_position"),
    path("length_of_tenure", Length_of_tenure_view, name="length_of_tenure"),
    path("courses_related_to_quality_management", Courses_related_to_quality_management_view, name="courses_related_to_quality_management"),
    path("other_management_system_trainings", Other_management_system_trainings_view, name="other_management_system_trainings"),
    path("code_of_conduct", Code_of_conduct_view, name="code_of_conduct"),
    path("statement_of_the_applicant", Statement_of_the_applicant_view, name="statement_of_the_applicant"),
    path("detailed_applicant/<int:user_id>/", Detailed_applicant_view, name="detailed_applicant"),

]