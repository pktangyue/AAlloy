# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Window.need_m'
        db.add_column(u'clip_window', 'need_m',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Window.need_z'
        db.add_column(u'clip_window', 'need_z',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Window.need_m'
        db.delete_column(u'clip_window', 'need_m')

        # Deleting field 'Window.need_z'
        db.delete_column(u'clip_window', 'need_z')


    models = {
        u'clip.material': {
            'Meta': {'object_name': 'Material'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clip.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.ProductName']"}),
            'window': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Window']"})
        },
        u'clip.productname': {
            'Meta': {'object_name': 'ProductName'},
            'formula': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clip.producttrim': {
            'Meta': {'object_name': 'ProductTrim'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Material']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Product']"}),
            'trim_length': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '3'})
        },
        u'clip.window': {
            'Meta': {'object_name': 'Window'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'need_m': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_z': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['clip']