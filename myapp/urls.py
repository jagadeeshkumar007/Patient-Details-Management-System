from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.home, name='home'),
    #path('index', views.index, name='index'),
    #path('counter', views.counter, name='counter')
    path('hospitallogin',views.hospitallogin,name='hospitallogin'),
    #path('logedin',views.logedin,name="logedin"),
    path('notlog',views.notlog,name="notlog"),
    path('pdata',views.pdata,name="pdata"),
    path('pdataview',views.pdataview,name="pdataview"),
    path('signup',views.signup,name='signup'),
    path('cont',views.cont,name='cont'),
    path('upload',views.upload,name='upload'),
    path('about',views.about,name='about'),
    path('verify',views.verify,name='verify'),
    path('patientlogin',views.patientlogin,name='patientlogin'),
    path('userdetails',views.userdetails,name='userdetails')
    #path('logout',views.logout,name='logout'),
    #path('sendmail',views.sendmail,name='sendmail'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)