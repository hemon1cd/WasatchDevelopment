from django.shortcuts import render
from express.models import UserLogin, Client, Product, Service, Aed, Battery, Eyewash
from django.shortcuts import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response as render, HttpResponse, HttpResponseRedirect, redirect
from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect
from django.template import RequestContext
#from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
#If you need to use something similar to the url template tag in your code
from django.core.urlresolvers import reverse
import datetime
#import timezone
from express.forms import UserLoginForm, UserProfileForm, ServiceInstallForm, ProductInstallForm, MaintForm
from django.db.models import Q
from django.contrib import auth


@login_required(login_url='/express/Templates/login')
def add_user(request,template_name="add_user.html"):
	if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    context['success'] = "Successfully added user!"
                except Exception, e:
                    context['error'] = "Error. %s" % e
            #return HttpResponseRedirect('/add_user_success/')

        context = {}
        context.update(csrf(request))

        context['form'] = UserCreationForm()
        print context
        return render(template_name, context, context_instance=RequestContext(request))

def add_user_success(request,template_name="add_user_success.html"):
    context = {}
    return render(template_name, context, context_instance=RequestContext(request))


def admin_emp_select(request,template_name="admin_emp_select.html"):
    context = {}

    return render(template_name, context, context_instance=RequestContext(request))

def base(request,template_name="base.html"):
	context = {}
	context['base'] = "base1"
	
	return render(template_name, context, context_instance=RequestContext(request))

def edit_add(request,template_name="edit_add.html"):
	context = {}
	context[''] = ""
	
	return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='/express/Templates/login')
def search(request,template_name="search.html"):
    context = {}

    clients = Client.objects.all().order_by('company_name')

    context['clients'] = clients

    datenow = datetime.datetime.now()
    context['datenow'] = datenow

    #one_client = Client.objects.get(id = Product.client)



    products = Product.objects.all()

    context['products'] = products

    # if request.method == 'POST':
    #
    #         form = SearchForm(request.POST)
    #         if form.is_valid():
    #                 return HttpResponseRedirect('/search/')
    # else:
    #     form = SearchForm()
    #
    #     context['form'] = form


    return render(template_name, context, context_instance=RequestContext(request))

    print products

@login_required(login_url='/express/Templates/login')
def home(request, template_name="home.html"):



    date1 = datetime.date.today()
    end_week = date1 + datetime.timedelta(7)

	# start_date = datetime.date.today()
	# end_date = datetime.date.today() + datetime.timedelta(days=30)
	# jon_date = datetime.date.today() + datetime.timedelta(days=60)
    context = {}

    products = Product.objects.filter(expiration_date__range=[date1,end_week]).order_by('client')

    context['products'] = products

    return render(template_name, context, context_instance=RequestContext(request))


def login(request):

    context = {}
    context.update(csrf(request))
    return render('login.html',context)

def auth_view(request):
    username = request.POST.get('username', ' ')
    password = request.POST.get('password', ' ')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/login/')

def logout(request,template_name="login.html"):
    context = {}
    try:
        context['do_not_show_menu'] = True
        logout(request)
        return HttpResponseRedirect('/login/')
    except:
        pass

	return render(template_name, context, context_instance=RequestContext(request))

def report(request,template_name="report.html"):
	context = {}
	context[''] = ""

	return render(template_name, context, context_instance=RequestContext(request))


# @login_required(login_url='/express/Templates/login')
# def service(request,template_name="service.html"):
# 	context = {}
#
#         myform = ServiceForm(data=request.POST or None)
#
#         if myform.is_valid():
#             try:
#                 myform.save()
#                 myform = ServiceForm()
#             except:
#                  pass
#
#         context['form'] = myform
#
#         return render(template_name, context, context_instance=RequestContext(request))

def employee(request):
	context = {}
	context[''] = ""
	
	return render(template_name, context, context_instance=RequestContext(request))


# @login_required(login_url='/express/Templates/login')
# def install(request, template_name="service.html"):
#     if request.POST:
#         form = InstallForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponseRedirect('/install/')
#     else:
#         form = InstallForm()
#
#     args = {}
#     args.update(csrf(request))
#
#     args['form'] = form
#
#     #return render_to_response('service.html', args)
#     return render(template_name, args, context_instance=RequestContext(request))

@login_required(login_url='/express/Templates/login')
def installing(request, template_name="service.html"):

    pform = ProductInstallForm(data=request.POST or None)

    if request.POST:
        if pform.is_valid():

            try:
                pform.save()
                Service.objects.create(
                    service_type = "I",
                    user_login = request.user,
                    client = pform.cleaned_data['client'],
                )
                return HttpResponseRedirect('service.html')
            except Exception, e:
                print e

    args = {}
    args.update(csrf(request))

    args['pform'] = pform

    return render(template_name, args, context_instance=RequestContext(request))


def client_product_list(request, template_name="clientproduct.html"):

    context = {}

    try:
        clients = Client.objects.get(pk= request.GET.get("client"))
        product = Product.objects.filter(client= clients).filter(company_name__startswith='UT Traffic Ops')
            #expiration_date__range={datetime.datetime.now(),datetime.timedelta(days=365)})

    except:

        product = Product.objects.filter()

    context['product']= product

    return render(template_name, context, context_instance=RequestContext(request))


@login_required(login_url='/express/Templates/login')
def maintenance(request, template_name="maintenance.html"):

    pform = ProductInstallForm(data=request.POST or None)

    if request.POST:
        if pform.is_valid():

            try:
                pform.save()
                Service.objects.create(
                    service_type = "M",
                    user_login = request.user,
                    client = pform.cleaned_data['client'],
                )
                return HttpResponseRedirect('/maintenance/')
            except Exception, e:
                print e

    args = {}
    args.update(csrf(request))

    args['pform'] = pform

    return render(template_name, args, context_instance=RequestContext(request))


@login_required(login_url='/express/Templates/login')
def report(request, template_name="report.html"):

    context = {}

    reports = Product.objects.all().order_by('client')

    context['reports'] = reports

    return render(template_name, context, context_instance=RequestContext(request))


