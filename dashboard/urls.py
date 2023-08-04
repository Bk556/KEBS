from django.urls import path
from dashboard.views import Dashboard_view

app_name = "dashboard"
urlpatterns = [
    path('dashboard/',Dashboard_view, name='dashboard'),
    path('dashboard/',Dashboard_view, name='membershipofficer dashboard'),
    path('dashboard/',Dashboard_view, name='detailed_applicant')
    #path("Dashboard",Dashboard, name="Dashboard"),
]