"""midgo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('main/', views.main),
    path('board/addBoard/', views.add_board),
    path('board/addBoard/summernote_uploadImage/', views.summernote_uploadImage),
    path('board/addBoard/write/', views.write_board),
    path('board/modify/', views.modify_article),
    path('board/read/<int:board_id>/', views.read_board),
    path('join/', views.join),
    path('join/join_check_id/', views.join_check_id),
    path('search/<str:search_value>/', views.search_article),
    path('join/check_join/', views.check_join),
    path('check_notification/<int:notification_id>/', views.check_notification),
    path('delete_notification/<int:notification_id>/', views.delete_notification),

    path('delete_checked_notification/', views.delete_checked_notification),
    path('delete_all_notification/', views.delete_all_notification),

    path('recognizeUserList/', views.show_unrecognized_users),
    path('recognizeUser/<str:user_id>/', views.recognize_user),

    path('recognizeUser/<str:user_id>/recognize/<str:user_grade>/', views.recognize),
    path('recognizeUser/<str:user_id>/unrecognize/', views.unrecognize),

    path('login_check/', views.login_check),
    path('login_page/', views.login_page),
    path('logout_page/', views.logout_page),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)