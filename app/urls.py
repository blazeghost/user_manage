from django.urls import path, include
from . import views


urlpatterns = [

    ################# URLS ###################
    path('', views.LoginPage, name='loginpage'),
    path('registerpage/', views.RegisterPage, name='registerpage'),
    path('index/', views.IndexPage, name='indexpage'),
    path('superloginpage/', views.SuperAdminLoginPage, name='superloginpage'),
    path('superindex/', views.SuperIndex, name='superindex'),
    path('addsuperuser/', views.SuperAddUser, name='addsuperuser'),
    path('superuserlist/', views.SuperUserList, name='superuserlist'),
    path('supereditpage/<int:pk>', views.SuperAdminEditPage, name='supereditpage'),
    path('visitordetails/', views.VisitorDetails, name='visitordetails'),
    path('admineditpage/<int:pk>', views.AdminEditPage, name='admineditpage'),
    path('securityeditpage/<int:pk>',
         views.SecurityEditPage, name='securityeditpage'),


    ################ FUNCTIONAL URLS ################
    path('superlogin/', views.SuperAdminLogin, name='superlogin'),
    path('superlogout/', views.SuperAdminLogout, name='superlogout'),
    path('register/', views.Register, name='register'),
    path('superadduser/', views.SuperAddUserDetail, name='superadduser'),
    path('superuserdelete/<int:pk>',
         views.SuperAdminDelete, name='superuserdelete'),
    path('superedit/<int:pk>', views.SuperAdminEdit,  name='superedit'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('profile/<int:pk>', views.Profile, name='profile'),
    path('visitorlist/', views.VisitorList, name='visitorlist'),
    path('addvisitor/<int:pk>', views.AddVisitor, name='addvisitor'),
    path('adminedit/<int:pk>', views.AdminEditVisitor, name='adminedit'),
    path('securityedit/<int:pk>', views.SecurityEditVisitor, name='securityedit'),
    path('admindelete/<int:pk>', views.AdminDelete, name='admindelete'),
    path('securitydelete/<int:pk>', views.SecurityDelete, name='securitydelete'),




]
