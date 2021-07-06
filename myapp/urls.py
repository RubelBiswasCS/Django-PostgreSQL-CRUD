from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name="home"),
   path('<int:pk>/delete_view',views.delete_view,name="delete-view"),
   path('<int:pk>/update_view',views.update_view,name="update-view"),
   # path('',views.add_record,name="home"),
]
