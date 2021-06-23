from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
	path('', views.loginPage, name="login"),
	path('index1/', views.index1, name='index1'),
	path('register/', views.registerPage, name="register"),
    path('index/',views.index,name="index"),
	path('news/',views.news,name="news"),
	path('overallrating/',views.overallrating,name="rating"),
	path('membership/',views.membership,name="membership"),
	path('creator/',views.creator,name="creator"),
	path('trainer/', views.trainer, name="trainer"),
	path('formup/', views.formup, name="formup"),
	path('fitnessresult/',views.fitnessresult,name="fitnessresult"),
	path('fitness/<str:pk>/', views.fitness, name="fitness"),
	path('logout/', views.logoutUser, name="logout"),
	path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('resultsdata/<str:obj>/', views.resultsData, name="resultsdata"),


]

urlpatterns+=staticfiles_urlpatterns() 
