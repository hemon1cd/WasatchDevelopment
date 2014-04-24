# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Service.service_id'
        db.delete_column(u'express_service', 'service_id')

        # Adding field 'Service.id'
        db.add_column(u'express_service', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Service.service_id'
        db.add_column(u'express_service', 'service_id',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=250, primary_key=True),
                      keep_default=False)

        # Deleting field 'Service.id'
        db.delete_column(u'express_service', u'id')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_service_date': ('django.db.models.fields.DateField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['express.Product']"}),
            'service_date': ('django.db.models.fields.DateField', [], {}),
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