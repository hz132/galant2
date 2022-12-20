from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('lesson/', LessonPageView, name='lesson'),
    path('individual/', IndividualPageView, name='individual'),
    path('lectures/', LecturesPageView, name='lectures'),
    path('record/', RecordPageView, name='record'),
    path('igor/', IgorPageView, name='igor'),
    path('zlata/', ZlataPageView, name='zlata'),
    path('irina/', IrinaPageView, name='irina'),
]