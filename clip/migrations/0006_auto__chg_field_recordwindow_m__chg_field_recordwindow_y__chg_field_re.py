# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'RecordWindow.m'
        db.alter_column(u'clip_recordwindow', 'm', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1))

        # Changing field 'RecordWindow.y'
        db.alter_column(u'clip_recordwindow', 'y', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1))

        # Changing field 'RecordWindow.x'
        db.alter_column(u'clip_recordwindow', 'x', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1))

        # Changing field 'RecordWindow.z'
        db.alter_column(u'clip_recordwindow', 'z', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1))

        # Changing field 'RecordProduct.length'
        db.alter_column(u'clip_recordproduct', 'length', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1))

    def backwards(self, orm):

        # Changing field 'RecordWindow.m'
        db.alter_column(u'clip_recordwindow', 'm', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'RecordWindow.y'
        db.alter_column(u'clip_recordwindow', 'y', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'RecordWindow.x'
        db.alter_column(u'clip_recordwindow', 'x', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'RecordWindow.z'
        db.alter_column(u'clip_recordwindow', 'z', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'RecordProduct.length'
        db.alter_column(u'clip_recordproduct', 'length', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'clip.producttrim': {
            'Meta': {'object_name': 'ProductTrim'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Material']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Product']"}),
            'trim_length': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '3'})
        },
        u'clip.record': {
            'Meta': {'object_name': 'Record'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'clip.recordproduct': {
            'Meta': {'object_name': 'RecordProduct'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Product']"}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Record']"})
        },
        u'clip.recordwindow': {
            'Meta': {'object_name': 'RecordWindow'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Record']"}),
            'window': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Window']"}),
            'x': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'y': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'z': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'})
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