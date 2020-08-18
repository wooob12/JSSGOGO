from django.urls import path
from .views import index, create, detail, delete, update, my_index, create_comment
## main 아래 있어서 .views로 해줌


urlpatterns = [
    path('', index, name="index"),
    path('my_index', my_index, name="my_index"),
    path('create/', create, name="create"),
    path('detail/<int:jss_id>', detail, name="detail"),
    path('delete/<int:jss_id>', delete, name="delete"),    
    path('update/<int:jss_id>', update, name="update"),

    # comment #
    path('create_comment/<int:jss_id>/', create_comment, name="create_comment"),
]