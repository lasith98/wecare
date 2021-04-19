from django.urls import path
from . import views
from . import update_views as update_views

app_name = "employee_management_system"

urlpatterns = [
    path('' , views.dashboard , name = "ems_home"),
    path('enroll_doctor' , views.enroll_new_doctor , name = "ems_enroll_doctor"),
    path('enroll_nurse' , views.enroll_new_nursing_officer , name = "ems_enroll_nurse"),
    path('enroll_h_professional' , views.enroll_new_health_professional , name = "ems_enroll_h_professional"),
    path('enroll_m_staff' ,views.enroll_new_management_staff ,name= "ems_enroll_m_staff"),

    path('new_salary_g' , views.create_new_salary_group , name = "new_salary_group"),
    path('update_salary_g' , views.update_salary_group , name = "ems_update_salary_group"),
    path('new_doctor_specialization', views.new_doctor_specialization , name = 'ems_new_specialization'),
    path('update_doctor_specialization' , views.update_delete_specialization , name = 'ems_update_doctor_specialization'),

    path('update_doctor' , update_views.update_doctor , name = 'ems_update_doctor'),
    path('update_nurse' , update_views.update_nurse , name = 'ems_update_nurse'),
    path('update_h_professional' , update_views.update_health_prof , name = 'ems_update_h_professional'),
    path('update_man_staff' , update_views.update_management_staff , name = 'ems_update_man_staff'),


    path('doctor' , views.doctor , name = "ems_doctor"),
    path('nursing_officer' , views.nursing_officer , name = 'ems_nursing_officer'),
    path('health_professional' , views.health_prof , name = 'emp_health_professional'),
    path('management_staff' , views.man_staff , name = 'emp_management_staff'),

]