from django.urls import path 
from . import views

urlpatterns=[
    path('' , views.index , name="index"),
    path('register/' , views.register , name="register"),
    path('login/' , views.login_user , name="login"),
    path('logout/' , views.logout_user , name="logout"),
    path('municipiltys/' , views.municilitys , name='municipiltys'),
    path('news/' , views.news , name='news'),
    path('map/' , views.map , name='map'),
    path('projects/' , views.project , name='projects'),
    path('municipilty_info/<str:slugy>' , views.municiplity_info , name='municiplity_info'),
    path('satitc/<str:slugy>' , views.munstatic , name='munstatic'),
    path('description/<str:slugy>' , views.dec_info ,name="dec_info"),
    path('add_decribe/<str:slugy>' , views.add_decribe , name='add_decribe'),
    path('check_decribe/' ,views.check_decribes , name='check_decribe'),
    path('into_decribe/<str:slugy>' , views.into_decribe , name='into_decribe'),
    path('post_describe/<str:slugy>' , views.post_decribe , name='post_decribe'),
    path('formulaire/<str:slugy>' , views.formulaire , name='formulaire'),
    path('delete_decribe_checked/<str:slugy>' , views.delete_decribe_checked , name='delete_decribe_checked'),     
    path('profile/<int:id>' , views.profile , name='profile'),
    path('add_comment/' , views.add_comment , name='add_comment'),
    path('create_municipality' , views.create_municipality , name='create_municipality'),
    path('delete_decribe/<str:slugy>' , views.delete_decribe , name='delete_describe'),
    path('visit_deccheck/' , views.visit_deccheck , name='visit_deccheck')
]