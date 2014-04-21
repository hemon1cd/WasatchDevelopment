from django.shortcuts import render
from express.models import UserLogin, Client, Product, Service, Aed, Battery, Eyewash
import datetime
from django.shortcuts import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response as render, HttpResponse, HttpResponseRedirect, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
#If you need to use something similar to the url template tag in your code
from django.core.urlresolvers import reverse
import datetime
from express.forms import UserLoginForm, UserProfileForm, ServiceForm
from django.db.models import Q


def admin_emp_edit_add(request,template_name="admin_emp_edit_add.html"):
	context = {}
	context['adminedit'] = "adminedit1" 
	
	return render(template_name, context, context_instance=RequestContext(request))

def admin_emp_select(request,template_name="admin_emp_select.html"):
	context = {}
	context[''] = ""
	
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

    #one_client = Client.objects.get(id = Product.client)



    products = Product.objects.all()

    context['products'] = products

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


def login(request,template_name="login.html"):

    context = {}
    context.update(csrf(request))
    next = None

    try:
        next = request.GET['next']

    except:
        next = ""


    auth_frm = AuthenticationForm(data=request.POST or None)
    context['form'] = auth_frm

    if auth_frm.is_valid():
        try:
            user = authenticate(username=auth_frm.cleaned_data['username'], password=auth_frm.cleaned_data['password'])
            login(request, user)
        except Exception:
            pass

            #return the same form and say login failed
            
	# See this? This is wrong. We don't redirect to templates, we redirect to views.
	# For example: HttpResponseRedirect('/userlogin')
	# I'm going to let you fix this one and the one under it. 
        return HttpResponseRedirect('/home/')

    return render(template_name, context, context_instance=RequestContext(request))

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


@login_required(login_url='/express/Templates/login')
def service(request,template_name="service.html"):
	context = {}

        if request.method == 'POST':

                form = ServiceForm(request.POST)
                if form.is_valid():

                        return HttpResponseRedirect('/home/')
        else:
            form = ServiceForm()

	    context['form'] = form
	


        clients = Client.objects.all().order_by('company_name')
        context['clients'] = clients

        locations = Product.objects.all()

        context['locations'] = locations

        products = Product.objects.all()

        context['products'] = products

        return render(template_name, context, context_instance=RequestContext(request))

def employee(request):
	context = {}
	context[''] = ""
	
	return render(template_name, context, context_instance=RequestContext(request))


