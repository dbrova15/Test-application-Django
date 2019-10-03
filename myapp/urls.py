from django.urls import path, include

from . import views

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),
    # path('add_data', views.add_data, name='add_data'),
    # path('data_del/id=<int:id_post>', views.del_data, name='del_data'),
    # path('data_view/id=<int:id_post>', views.del_view, name='del_data'),
    # path('edit_post/id=<int:id_post>', views.edit_data, name='edit_data'),
    path('', include('social_django.urls', namespace='social')),
]
