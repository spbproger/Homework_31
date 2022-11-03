from django.urls import path
from selections import views


urlpatterns = [
    path('', views.SelectionListView.as_view(), name='selections'),
    path('<int:pk>/', views.SelectionDetailView.as_view(), name='selection'),
    path('create/', views.SelectionCreateView.as_view(), name='create_selection'),
    path('update/<int:pk>/', views.SelectionUpdateView.as_view(), name='update_selection'),
    path('delete/<int:pk>/', views.SelectionDeleteView.as_view(), name='delete_selection'),
]