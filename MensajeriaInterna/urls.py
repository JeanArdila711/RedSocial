from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('send_message/', views.send_message, name='send_message_no_receiver'),  # No receiver ID passed
    path('send_message/<int:user_reciever_id>/', views.send_message, name='send_message_to_user'),  # With receiver ID
    path('mirar_mensaje/<int:message_id>/', views.mirar_mensaje, name='mirar_mensaje'),

]
