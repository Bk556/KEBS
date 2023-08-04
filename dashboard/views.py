from django.shortcuts import render,redirect
from membership.models import Membership_applications

# Create your views here.
def Dashboard_view(request):
    user = request.user
    if user.groups.filter(name='client').exists():
        return render(request, "dashboard.html")
    elif user.groups.filter(name='membership_officer').exists():
        completed_applications = []

        for member in Membership_applications.objects.all():
            user_id = member.Member.id
            first_name = member.Member.first_name
            last_name = member.Member.last_name
            email = member.Member.email

            completed_applications.append({"user_id":user_id, "first_name":first_name, "last_name":last_name, "email":email})

        #completed_applications = Membership_applications.objects.all().values()
        # import pdb;pdb.set_trace()
        return render(request, "membershipofficer dashboard.html", {"data": completed_applications})
    #Dashboard(request)
    #return render(request,"dashboard.html")

