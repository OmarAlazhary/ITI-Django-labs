from django.urls import path
from . import views

urlpatterns = [
    path('traineelist/', views.TraineeListView.as_view(), name='trainee_list'),
    path('add_trainee/', views.AddTraineeView.as_view() , name='add_trainee'),
    path('update_trainee/<int:id>/', views.UpdateTraineeView.as_view(), name='update_trainee'),
    path('delete_trainee/<int:pk>/', views.TraineeDeleteView.as_view(), name='delete_trainee'),
]

