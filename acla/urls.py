from django.urls import path

from .views import (
    alert_undefined_view,
    alert_true_positive_view,
    alert_false_positive_view,
    alert_detail,
    update_alert
    )

urlpatterns = [
    path('undefined/', alert_undefined_view, name='undefined_alert'),
    path('true_positive/', alert_true_positive_view, name='true_positive'),
    path('false_positive/', alert_false_positive_view, name='false_positive'),
    path('<int:id>/', alert_detail, name='alert_detail'),
    path('<int:id>/update', update_alert, name='update_alert'),
]