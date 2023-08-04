from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registration_type(models.Model):
    choices_register=[("New","New"),("Existing","Existing"),]
    reg_type = models.CharField(max_length=15, choices=choices_register)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True, unique=True)

    # def save(self, *args, **kwargs):
    #     current_user = self.request.session['userid']
    #     self.user = current_user
    #     return super(Registration_type, self).save(*args, **kwargs)

class Member_type(models.Model):
    choices_member = [("Student member","Student member(0 and ongoing student)"),("Affiliate member","Affiliate member(graduated and 0 years)"),("Associate member","Associate memeber(1-2 years)"),("Full member","Full member(3 years)")]
    member_type = models.CharField(max_length=30, choices=choices_member)
    user = models.ForeignKey(User,on_delete=models.CASCADE, unique=True)
    years_trained = models.CharField(max_length=3)

class Applicant_details(models.Model):
    choices_tittle = [("Mr", "Mr"),("Mrs", "Mrs"),("Prof", "Prof"),("Miss","Miss")]
    tittle = models.CharField(max_length=10, choices=choices_tittle, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    identification_card = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    profession = models.CharField(max_length=30)
    organization_name = models.CharField(max_length=50)
    organization_address = models.CharField(max_length=100)
    organization_telephone = models.CharField(max_length=30)
    business_email = models.CharField(max_length=30)
    choices_nature_of_organization = [("private","private"),("public",("public"))]
    nature_of_organization = models.CharField(max_length=30, choices=choices_nature_of_organization, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, unique=True)

class Academic_qualification(models.Model):
    name_of_institution = models.CharField(max_length=50)
    date_from = models.DateTimeField(max_length=30)
    date_to = models.DateTimeField(max_length=30)
    choices_course_duration_in_years = [("1","1"),("2","2"),("3","3"),("4","4"),("5","5")]
    course_duration_in_years = models.CharField(max_length=4, choices=choices_course_duration_in_years, null=True, blank=True)
    certificate_awarded = models.CharField(max_length=30)
    certificate_file = models.FileField(upload_to='documents/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)


class Specialized_area(models.Model):
    Trainer = models.BooleanField(default=False)
    Auditor = models.BooleanField(default=False)
    Assesor = models.BooleanField(default=False)
    Implementor = models.BooleanField(default=False)
    Management_representative = models.BooleanField(default=False)
    Process_owner = models.BooleanField(default=False)
    Member_of_quality_improvement_team = models.BooleanField(default=False)
    Quality_assurance_manager = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

class Information_on_present_position(models.Model):
    description_on_current_quality = models.TextField(max_length=50)
    any_other_specify = models.CharField(max_length=200)
    YEAR_CHOICES = [(i, i) for i in range(1, 11)]  # Options 1 to 10 years

    # Choices for months
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]  # Options 1 to 12 months
    years = models.IntegerField(choices=YEAR_CHOICES)
    months = models.IntegerField(choices=MONTH_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

class Length_of_tenure(models.Model):
    Name_of_organization = models.CharField(max_length=30)
    date_from = models.DateField(max_length=30)
    date_to = models.DateField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

class Courses_related_to_quality_management(models.Model):
    Course = models.CharField(max_length=30)
    Course_duration_in_years = models.IntegerField()
    Organization = models.CharField(max_length=30)
    Certificate_awarded = models.CharField(max_length=30)
    certificate_file = models.FileField(upload_to='documents/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

class Other_management_system_trainings(models.Model):
    Course = models.CharField(max_length=30)
    Course_duration_in_years = models.IntegerField()
    Organization = models.CharField(max_length=30)
    Certificate_awarded = models.CharField(max_length=30)
    certificate_file = models.FileField(upload_to='documents/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

class Code_of_conduct(models.Model):
    I_agree = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

class Statement_of_the_applicant(models.Model):
    Full_name_of_the_applicant = models.CharField(max_length=50)
    Date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

class Membership_applications(models.Model):
        Membership_officer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Mo")
        status = models.CharField(max_length=50, default='pending')
        Comments = models.CharField(max_length=100)
        Member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Me", null=True, blank=True)
        #Member = models.CharField(max_length=150, choices=[(user.username, user.username) for user in User.objects.all()], null=True, blank=True)











