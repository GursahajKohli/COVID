from django.urls import path,include
from .views import upload_view,index_view

app_name = 'classification_app'
urlpatterns = [
    path("",index_view,name="index_view"),
    #path("choice/",choice_view,name="choice_view"),
    path("upload/",upload_view,name='upload_view'),

]
