from django.urls import path
from .import views
urlpatterns = [
            path('',views.Projects),
            path('Project/<str:pk>',views.Project),
            path('englishpage/',views.englishpage),

]