from django.urls import include, path

from .views import DepartmentView,DepartmentPersonalView

urlpatterns = [
    path('', DepartmentView.as_view()),
    path('department/<str:department>/', DepartmentPersonalView.as_view()),
    
]
