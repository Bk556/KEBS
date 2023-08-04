from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import Registration_type_forms,Member_type_forms,Applicant_details_forms,Academic_qualification_forms,Specialized_area_forms,Information_on_present_position_forms,Length_of_tenure_forms,Courses_related_to_quality_management_forms,Other_management_system_trainings_forms,Code_of_conduct_forms,Statement_of_the_applicant_forms
from membership.models import Member_type,Registration_type,Applicant_details,Academic_qualification,Specialized_area,Information_on_present_position,Length_of_tenure,Courses_related_to_quality_management,Other_management_system_trainings,Code_of_conduct,Statement_of_the_applicant,Membership_applications
# Create your views here.
@login_required
def Registration_type_view(request):
    try:
        registration_type = Registration_type.objects.get(user=request.user)
        form = Registration_type_forms(request.POST or None, instance=registration_type)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("membership:membertype")
        else:
            form = Registration_type_forms(instance=registration_type)

    except Registration_type.DoesNotExist:
        form = Registration_type_forms(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                member_type = form.save(commit=False)
                member_type.user = request.user
                member_type.save()
                return redirect("membership:membertype")

    return render(request, "regtype.html", {"context": form})
#    form = Registration_type_forms()

#   if request.method == "POST":
#        form = Registration_type_forms(request.POST)

#        if form.is_valid():
#            registration_type = form.save(commit=False)
#            registration_type.user = request.user
#            registration_type.save()
#            return redirect("membership:membertype")

#    return render(request, "regtype.html", {"context": form})
@login_required

def Member_type_view(request):
    try:
        member_type = Member_type.objects.get(user=request.user)
        form = Member_type_forms(request.POST or None, instance=member_type)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("membership:applicant_details")
        else:
            form = Member_type_forms(instance=member_type)

    except Member_type.DoesNotExist:
        form = Member_type_forms(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                member_type = form.save(commit=False)
                member_type.user = request.user
                member_type.save()
                return redirect("membership:applicant_details")

    return render(request, "membertype.html", {"context": form})

# @login_required
# def Member_type_view(request):
#     form = Member_type_forms()
#
#     if request.method == "POST":
#       form = Member_type_forms(request.POST)
#
#         if form.is_valid():
#             member_type = form.save(commit=False)
#             member_type.user = request.user
#             member_type.save()
#            return redirect("membership:applicant details")
#
#    return render(request,"membertype.html",{"context":form})

@login_required
def Applicant_details_view(request):
    initial_data = {
        "first_name": request.session['firstname'],
        "last_name": request.session['lastname'],
        "email": request.session['email']

    }
    form = Applicant_details_forms(request.POST or None, initial=initial_data)

    try:
        applicant_details = Applicant_details.objects.get(user=request.user)
        form = Applicant_details_forms(request.POST or None, instance=applicant_details, initial=initial_data)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("membership:academic_qualification")
        else:
            form = Applicant_details_forms(instance=applicant_details, initial=initial_data)

    except Applicant_details.DoesNotExist:
        form = Applicant_details_forms(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                member_type = form.save(commit=False)
                member_type.user = request.user
                member_type.save()
                return redirect("membership:academic_qualification")

    return render(request, "applicant_details.html", {"context": form})



#    if request.method == "POST":
#        form = Applicant_details_forms(request.POST)

#       if form.is_valid():
#            applicant_details = form.save(commit=False)
#            applicant_details.user = request.user
#            applicant_details.save()
#           return redirect("membership:academic qualification")
#    #import pdb;pdb.set_trace()
#    return render(request,"applicant_details.html",{"context":form})

@login_required
def Academic_qualification_view(request):
    try:
        academic_qualification = Academic_qualification.objects.get(user=request.user)
        form = Academic_qualification_forms(request.POST, request.FILES, instance=academic_qualification)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("membership:specialized_area")
        else:
            form = Academic_qualification_forms(instance=academic_qualification)

    except Academic_qualification.DoesNotExist:
        form = Academic_qualification_forms(request.POST, request.FILES)

        if request.method == "POST":
            if form.is_valid():
                academic_qualification = form.save(commit=False)
                academic_qualification.user = request.user
                academic_qualification.save()
                return redirect("membership:specialized_area")

    return render(request, "academic_qualification.html", {"context": form})
#    form = Academic_qualification_forms()

#    if request.method == "POST":
#        form = Academic_qualification_forms(request.POST, request.FILES)

#        if form.is_valid():
#            academic_qualification = form.save(commit=False)
#            academic_qualification.user = request.user
#            academic_qualification.save()
#            return redirect("membership:specialized area")

#    return render(request,"academic_qualification.html",{"context":form})
@login_required
def Specialized_area_view(request):
    try:
        specialized_area = Specialized_area.objects.get(user=request.user)
        form = Specialized_area_forms(request.POST or None, instance=specialized_area)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("membership:information_on_present_position")
        else:
            form = Specialized_area_forms(instance=specialized_area)

    except Specialized_area.DoesNotExist:
        form = Specialized_area_forms(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                specialized_area = form.save(commit=False)
                specialized_area.user = request.user
                specialized_area.save()
                return redirect("membership:information_on_present_position")

    return render(request, "specialized_area.html", {"context": form})
#    form = Specialized_area_forms()

#    if request.method == "POST":
#        form = Specialized_area_forms(request.POST)

#        if form.is_valid():
#            specialized_area = form.save(commit=False)
#            specialized_area.user = request.user
#            specialized_area.save()
#           return redirect("membership:information on present position")


#    return render(request,"specialized_area.html",{"context":form})
@login_required
def Information_on_present_position_view(request):
    try:
        information_on_present_position = Information_on_present_position.objects.get(user=request.user)
        form = Information_on_present_position_forms(request.POST or None, instance=information_on_present_position)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("membership:length_of_tenure")
        else:
            form = Information_on_present_position_forms(instance=information_on_present_position)

    except Information_on_present_position.DoesNotExist:
        form = Information_on_present_position_forms(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                information_on_present_position = form.save(commit=False)
                information_on_present_position.user = request.user
                information_on_present_position.save()
                return redirect("membership:length_of_tenure")

    return render(request, "information_on_present_position.html", {"context": form})
#    form = Information_on_present_position_forms()

#    if request.method == "POST":
#        form = Information_on_present_position_forms(request.POST)

#        if form.is_valid():
#            information_on_present_position = form.save(commit=False)
#            information_on_present_position.user = request.user
#            information_on_present_position.save()
#            return redirect("membership:length of tenure")


#    return render(request,"information_on_present_position.html",{"context":form})
@login_required
def Length_of_tenure_view(request):
    try:
        length_of_tenure = Length_of_tenure.objects.get(user=request.user)
        form = Length_of_tenure_forms(request.POST or None, instance=length_of_tenure)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("membership:courses_related_to_quality_management")
        else:
            form = Length_of_tenure_forms(instance=length_of_tenure)

    except Length_of_tenure.DoesNotExist:
        form = Length_of_tenure_forms(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                length_of_tenure = form.save(commit=False)
                length_of_tenure.user = request.user
                length_of_tenure.save()
                return redirect("membership:courses_related_to_quality_management")

    return render(request, "length_of_tenure.html", {"context": form})
#    form = Length_of_tenure_forms()

#   if request.method == "POST":
#        form = Length_of_tenure_forms(request.POST)

#        if form.is_valid():
#            length_of_tenure = form.save(commit=False)
#            length_of_tenure.user = request.user
#            length_of_tenure.save()
#           return redirect("membership:courses related to quality management")


#    return render(request,"length_of_tenure.html",{"context":form})
@login_required
def Courses_related_to_quality_management_view(request):
    try:
        courses_related_to_quality_management = Courses_related_to_quality_management.objects.get(user=request.user)
        form = Courses_related_to_quality_management_forms(request.POST, request.FILES, instance=courses_related_to_quality_management)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("membership:other_management_system_trainings")
        else:
            form = Courses_related_to_quality_management_forms(instance=courses_related_to_quality_management)

    except Courses_related_to_quality_management.DoesNotExist:
        form = Courses_related_to_quality_management_forms(request.POST, request.FILES)

        if request.method == "POST":
            if form.is_valid():
                courses_related_to_quality_management = form.save(commit=False)
                courses_related_to_quality_management.user = request.user
                courses_related_to_quality_management.save()
                return redirect("membership:other_management_system_trainings")


    return render(request, "courses_related_to_quality_management.html", {"context": form})
#    form = Courses_related_to_quality_management_forms()

#    if request.method == "POST":
#        form = Courses_related_to_quality_management_forms(request.POST, request.FILES)

#        if form.is_valid():
#            courses_related_to_quality_management = form.save(commit=False)
#            courses_related_to_quality_management.user = request.user
#            courses_related_to_quality_management.save()
#            return redirect("membership:other management system trainings")


#    return render(request,"courses_related_to_quality_management.html",{"context":form})
@login_required
def Other_management_system_trainings_view(request):
    try:
        other_management_system_trainings = Other_management_system_trainings.objects.get(user=request.user)
        form = Other_management_system_trainings_forms(request.POST, request.FILES, instance=other_management_system_trainings)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("membership:code_of_conduct")
        else:
            form = Other_management_system_trainings_forms(instance=other_management_system_trainings)

    except Other_management_system_trainings.DoesNotExist:
        form = Other_management_system_trainings_forms(request.POST, request.FILES)

        if request.method == "POST":
            if form.is_valid():
                other_management_system_trainings = form.save(commit=False)
                other_management_system_trainings.user = request.user
                other_management_system_trainings.save()
                return redirect("membership:code_of_conduct")

    return render(request, "other_management_system_trainings.html", {"context": form})
#    form = Other_management_system_trainings_forms()

#    if request.method == "POST":
#        form = Other_management_system_trainings_forms(request.POST, request.FILES)

#        if form.is_valid():
#            other_management_system_trainings = form.save(commit=False)
#            other_management_system_trainings.user = request.user
#            other_management_system_trainings.save()
#            return redirect("membership:code of conduct")


#    return render(request,"other_management_system_trainings.html",{"context":form})
@login_required
def Code_of_conduct_view(request):
    try:
        code_of_conduct = Code_of_conduct.objects.get(user=request.user)
        form = Code_of_conduct_forms(request.POST or None, instance=code_of_conduct)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("membership:statement_of_the_applicant")
        else:
            form = Code_of_conduct_forms(instance=code_of_conduct)

    except Code_of_conduct.DoesNotExist:
        form = Code_of_conduct_forms(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                code_of_conduct = form.save(commit=False)
                code_of_conduct.user = request.user
                code_of_conduct.save()
                return redirect("membership:statement_of_the_applicant")

    return render(request, "code_of_conduct.html", {"context": form})
#    form = Code_of_conduct_forms()

#    if request.method == "POST":
#        form = Code_of_conduct_forms(request.POST)

#        if form.is_valid():
#            code_of_conduct = form.save(commit=False)
#            code_of_conduct.user = request.user
#            code_of_conduct.save()
#            return redirect("membership:statement of the applicant")


#    return render(request,"code_of_conduct.html",{"context":form})
@login_required
def Statement_of_the_applicant_view(request):
    try:
        statement_of_the_applicant = Statement_of_the_applicant.objects.get(user=request.user)
        form = Statement_of_the_applicant_forms(request.POST or None, instance=statement_of_the_applicant)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                # Save the applicant's name to the Membership_officer model
                userid = request.user
                Membership_applications.objects.get_or_create(
                    # Membership_officer=request.user,
                    status='pending',
                    Comments='',
                    Member=userid
                )

                return render(request, 'confirmation.html',{'applicant_name': userid, 'your_name': 'Your Name'})
                #return redirect("membership:confirmation")
        else:
            form = Statement_of_the_applicant_forms(instance=statement_of_the_applicant)

    except Statement_of_the_applicant.DoesNotExist:
        form = Statement_of_the_applicant_forms(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                statement_of_the_applicant = form.save(commit=False)
                statement_of_the_applicant.user = request.user
                statement_of_the_applicant.save()
                # Save the applicant's name to the Membership_officer model
                username = request.user.username
                membership_officer, _ = Membership_applications.objects.get_or_create(
                    Membership_officer=request.user,
                    status='pending',
                    Comments='',
                    Member=username
                )

                return render(request, 'confirmation.html', {'applicant_name': username, 'your_name': 'Your Name'})
                #return redirect("membership:confirmation")

    return render(request, "statement_of_the_applicant.html", {"context": form})
#    form = Statement_of_the_applicant_forms()

#    if request.method == "POST":
#        form = Statement_of_the_applicant_forms(request.POST)

#        if form.is_valid():
#            statement_of_the_applicant = form.save(commit=False)
#            statement_of_the_applicant.user = request.user
#            statement_of_the_applicant.save()
#            return redirect("membership:membership officer detail")


#    return render(request,"statement_of_the_applicant.html",{"context":form})
#@login_required
#def Membership_officer_view(request):
#    if request.method == 'POST':
        # Process the applicant forms and save the data
        # ...

        # Create a new Membership_officer object and save it
#        membership_officer = Membership_officer.objects.create(
#            Membership_officer=request.user,
#            status='pending',
#            Comments=''
#        )

        # Redirect the user to the Membership_officer detail page
#        return redirect('membership_officer_detail', pk=membership_officer.pk)

#    else:
        # Render the form for the applicant to fill out
#        return render(request, 'membership_officer/form.html')

def Detailed_applicant_view(request, user_id):
    reg_type = Registration_type.objects.get(user=user_id)
    member_type = Member_type.objects.get(user=user_id)
    applicant_detail = Applicant_details.objects.get(user=user_id)
    academic_qualification = Academic_qualification.objects.get(user=user_id)
    specialized_area = Specialized_area.objects.get(user=user_id)
    information_on_present_position = Information_on_present_position.objects.get(user=user_id)
    length_of_tenure = Length_of_tenure.objects.get(user=user_id)
    courses_related_to_quality_management = Courses_related_to_quality_management.objects.get(user=user_id)
    other_management_system_trainings = Other_management_system_trainings.objects.get(user=user_id)
    code_of_conduct = Code_of_conduct.objects.get(user=user_id)
    statement_of_the_applicant = Statement_of_the_applicant.objects.get(user=user_id)


    data = {
        "reg_type":reg_type,
        "member_type":member_type,
        "applicant_detail":applicant_detail,
        "academic_qualification":academic_qualification,
        "specialized_area":specialized_area,
        "information_on_present_position":information_on_present_position,
        "length_of_tenure":length_of_tenure,
        "courses_related_to_quality_management":courses_related_to_quality_management,
        "other_management_system_trainings":other_management_system_trainings,
        "code_of_conduct":code_of_conduct,
        "statement_of_the_applicant":statement_of_the_applicant
    }
    return render(request,'detailed_applicant.html',{"data":data})