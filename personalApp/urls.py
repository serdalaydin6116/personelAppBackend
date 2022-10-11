from django.urls import include, path

from .views import DepartmentView

urlpatterns = [
    path('', DepartmentView.as_view()),
    
]
