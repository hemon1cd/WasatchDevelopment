# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserLogin'
        db.create_table(u'express_userlogin', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('user_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'express', ['UserLogin'])

        # Adding model 'Client'
        db.create_table(u'express_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contact_first_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('contact_last_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('phone_nbr', self.gf('django.db.models.fields.CharField')(max_length=12, null=True)),
        ))
        db.send_create_signal(u'express', ['Client'])

        # Adding model 'Product'
        db.create_table(u'express_product', (
            ('product_id', self.gf('django.db.models.fields.CharField')(max_length=250, primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('product_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('expiration_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['express.Client'])),
        ))
        db.send_create_signal(u'express', ['Product'])

        # Adding model 'Aed'
        db.create_table(u'express_aed', (
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['express.Product'], primary_key=True)),
            ('aed_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'express', ['Aed'])

        # Adding model 'Battery'
        db.create_table(u'express_battery', (
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['express.Product'], primary_key=True)),
            ('aed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['express.Aed'])),
        ))
        db.send_create_signal(u'express', ['Battery'])

        # Adding model 'Eyewash'
        db.create_table(u'express_eyewash', (
            ('primary_secondary', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['express.Product'], primary_key=True)),
            ('eyewash_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'express', ['Eyewash'])

        # Adding model 'Service'
        db.create_table(u'express_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('service_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('expiration_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('user_login', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['express.UserLogin'])),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['express.Client'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['express.Product'])),
        ))
        db.send_create_signal(u'express', ['Service'])


    def backwards(self, orm):
        # Deleting model 'UserLogin'
        db.delete_table(u'express_userlogin')

        # Deleting model 'Client'
        db.delete_table(u'express_client')

        # Deleting model 'Product'
        db.delete_table(u'express_product')

        # Deleting model 'Aed'
        db.delete_table(u'express_aed')

        # Deleting model 'Battery'
        db.delete_table(u'express_battery')

        # Deleting model 'Eyewash'
        db.delete_table(u'express_eyewash')

        # Deleting model 'Service'
        db.delete_table(u'express_service')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'express.aed': {
            'Meta': {'object_name': 'Aed'},
            'aed_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['express.Product']", 'primary_key': 'True'})
        },
        u'express.battery': {
            'Meta': {'object_name': 'Battery'},
            'aed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['express.Aed']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['express.Product']", 'primary_key': 'True'})
        },
        u'express.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_nbr': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'})
        },
        u'express.eyewash': {
            'Meta': {'ordering': "['eyewash_type']", 'object_name': 'Eyewash'},
            'eyewash_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'primary_secondary': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['express.Product']", 'primary_key': 'True'})
        },
        u'express.product': {
            'Meta': {'ordering': "['-expiration_date', 'product_type']", 'object_name': 'Product'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['express.Client']"}),
            'expiration_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'product_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'primary_key': 'True'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'express.service': {
            'Meta': {'ordering': "['service_type', '-service_date', 'client']", 'object_name': 'Service'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['express.Client']"}),
            'expiration_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['express.Product']"}),
            'service_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'service_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_login': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['express.UserLogin']"})
        },
        u'express.userlogin': {
            'Meta': {'object_name': 'UserLogin'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['express']