from django.urls import path, include
from rest_framework import routers

from .views import EntryView, CSVParserView


router = routers.SimpleRouter()
router.register(r'entry', EntryView)

app_name = 'app'
urlpatterns = [
    path('', include(router.urls)),
    path('csv-parser/', CSVParserView.as_view()),
]
