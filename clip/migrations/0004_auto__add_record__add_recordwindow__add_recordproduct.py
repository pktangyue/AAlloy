# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Record'
        db.create_table(u'clip_record', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'clip', ['Record'])

        # Adding model 'RecordWindow'
        db.create_table(u'clip_recordwindow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Record'])),
            ('window', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Window'])),
            ('x', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('y', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('m', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('z', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'clip', ['RecordWindow'])

        # Adding model 'RecordProduct'
        db.create_table(u'clip_recordproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Record'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Product'])),
            ('length', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'clip', ['RecordProduct'])


    def backwards(self, orm):
        # Deleting model 'Record'
        db.delete_table(u'clip_record')

        # Deleting model 'RecordWindow'
        db.delete_table(u'clip_recordwindow')

        # Deleting model 'RecordProduct'
        db.delete_table(u'clip_recordproduct')


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
        u'clip.record': {
            'Meta': {'object_name': 'Record'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'clip.recordproduct': {
            'Meta': {'object_name': 'RecordProduct'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Product']"}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Record']"})
        },
        u'clip.recordwindow': {
            'Meta': {'object_name': 'RecordWindow'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Record']"}),
            'window': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Window']"}),
            'x': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'y': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'z': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
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