from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.dashboard, name="dashboard"),
    path('user/',views.userPage, name="user_page"),


    path('apply_bursary/', views.accountApplyBursary, name="apply_bursary"),

    path('bursaries/', views.bursaries, name="bursaries"),
    path('student/<str:pk_test>/', views.student, name="student"),

    path('create_application/<str:pk>/',views.createApplication, name="create_application"),
    path('update_application/<str:pk>/',views.updateApplication, name="update_application"),
    path('delete_application/<str:pk>/', views.deleteApplication, name="delete_application"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="bursary/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="bursary/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="bursary/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="bursary/password_reset_done.html"),
         name="password_reset_complete"),

]
