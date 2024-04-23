from django.urls import path

from bboard.views import index, by_rubric

urlpatterns = [
#    path('<int:rubric_id>/', by_rubric),# 57
    path('<int:rubric_id>/', by_rubric, name='by_rubric'), # стр 61
    path('', index),
]