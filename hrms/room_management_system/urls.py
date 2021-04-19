
from django.urls import path, include
from . import views

app_name = "room_management_system"

urlpatterns = [
    path('add_room' , views.add_room , name = 'rms_add_room'),
    path('update_room' , views.update_room , name = 'rms_update_room'),
    path('delete_room' , views.delete_room , name = 'rms_delete_room'),
    path('view_rooms' , views.room_list , name = "rms_view_rooms"),
    path('s_alocate_doc' , views.allocate_doc_r , name = 'rms_allocate_doc'),
    path('checked_room' , views.allocate_room , name = 'rms_checked_room'),
    path('allocate_nurses' , views.allocate_nurses , name = 'rms_allocate_nurses')

]