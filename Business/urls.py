from django.urls import path
from . import views

urlpatterns = [
    path('',views.business_create),
    path('add/',views.product_create),
    
    path('Views/',views.product_list),
 	# path('Create/',views.bank_create,name="bank_create"),
    # path('About Us/',views.about, name="about us"),
    # path('Applicant/',views.create_loan_application, name="applicant"),
    # path('Views/<int:business_name_id>/',views.product_list),
]