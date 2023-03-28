from . import views
from django.urls import path
app_name= 'placeapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>/', views.update, name='update'),
    path('del/<int:id>/', views.delete, name='delete')
]