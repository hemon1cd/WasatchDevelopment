from django.db import models
from django.contrib.auth.models import User
import datetime
#import timezone

class UserLogin (models.Model):

    user_types = (
    ('A','Admin'),
    ('U','User'),
    )
    user = models.OneToOneField(User, primary_key=True)
    user_type = models.CharField(max_length=50, choices=user_types)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __unicode__( self ):
		return self.user.username

class Client (models.Model):
    company_name = models.CharField(max_length=50, null=False)
    contact_first_name = models.CharField(max_length=50, null=True)
    contact_last_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=250, null=True)
    phone_nbr = models.CharField(max_length=12, null=True)

    def __unicode__( self ):
		return self.company_name


class Product (models.Model):

	class Meta:
		ordering = ['-expiration_date', 'product_type']

	product_types = (
	('AED','AED'),
	#('B','Battery'),
	('EyeWash','EyeWash'),
	)
	product_id = models.CharField(max_length=250, primary_key=True)
	location = models.CharField(max_length=250, null=True)
	product_type = models.CharField(max_length=50, choices=product_types)
	expiration_date = models.DateField('Date Expired', null=True)
	client = models.ForeignKey('client')

	def __unicode__( self ):
		return self.product_id


class Aed (models.Model):



	product = models.ForeignKey ('Product', primary_key=True)
	aed_type = models.CharField(max_length=50)

	def __unicode__( self ):
		return self.product_id

class Battery (models.Model):
	product = models.ForeignKey ('Product', primary_key=True)
	aed = models.ForeignKey('Aed')

	def __unicode__( self ):
		return self.product_id

class Eyewash (models.Model):

	class Meta:
		ordering = ['eyewash_type']

	primary_secondarys = (
	('P', 'Primary'),
	('S', 'Secondary'),
	)
	primary_secondary = models.CharField(max_length=50, choices=primary_secondarys)
	product = models.ForeignKey ('Product', primary_key=True)
	eyewash_type = models.CharField(max_length=50)


	def __unicode__( self ):
		return self.product_id


class Service (models.Model):

	class Meta:
		ordering = ['service_type', '-service_date', 'client']

	service_types = (
	('M', 'Maintenance'),
	('I', 'Install'),
	)
	service_id = models.CharField(max_length=250, primary_key=True)
	service_type = models.CharField(max_length=50, choices=service_types)
	service_date = models.DateField ('Date Serviced')
	expiration_date = models.DateField ('Expiration Date', null=True)
	user_login = models.ForeignKey('UserLogin')
	client = models.ForeignKey('Client')
	product = models.ForeignKey('Product')

	def __unicode__( self ):
		return self.service_id
















