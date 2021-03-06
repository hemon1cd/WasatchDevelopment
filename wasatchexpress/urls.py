from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
admin.autodiscover()

urlpatterns = patterns('',
	
    url(r'^admin/', include(admin.site.urls)),
	url(r'^userlogin','express.views.employee',name="Employee"),
	url(r'^add_user','express.views.add_user',name="add_user"),
    url(r'^add_user_success','express.views.add_user_success',name="add_user_success"),
	url(r'^admin_emp_select','express.views.admin_emp_select',name="admin_emp_select"),
	url(r'^base','express.views.base',name="base"),
	url(r'^edit_add','express.views.edit_add',name="edit_add"),
	url(r'^home','express.views.home',name="home"),
	url(r'^login','express.views.login',name="login"),
	url(r'^report','express.views.report',name="report"),
	url(r'^search','express.views.search',name="search"),
#	url(r'^service','express.views.service',name="service"),
	url(r'^logout','express.views.login',name="logout"),
    url(r'^auth/','express.views.auth_view',name="auth_view"),
#    url(r'^install/', 'express.views.install', name="install"),
    url(r'^installing/', 'express.views.installing', name="installing"),
    url(r'^client_product_list/', 'express.views.client_product_list', name="client_product_list"),
    url(r'^maintenance/', 'express.views.maintenance', name="maintenance"),



)
