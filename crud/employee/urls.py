
from django.urls import path  
from employee import views  

urlpatterns = [
    path("",views.login_page,name='login'),
    path('show/',views.show),
    path('add/', views.add),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.delete),

]  