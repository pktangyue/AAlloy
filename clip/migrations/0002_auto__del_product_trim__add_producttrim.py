# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Product_trim'
        db.delete_table(u'clip_product_trim')

        # Adding model 'ProductTrim'
        db.create_table(u'clip_producttrim', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('window', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Window'])),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Material'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Product'])),
            ('trim_length', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=3)),
        ))
        db.send_create_signal(u'clip', ['ProductTrim'])


    def backwards(self, orm):
        # Adding model 'Product_trim'
        db.create_table(u'clip_product_trim', (
            ('trim_length', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=3)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Product'])),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Material'])),
            ('window', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Window'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'clip', ['Product_trim'])

        # Deleting model 'ProductTrim'
        db.delete_table(u'clip_producttrim')


    models = {
        u'clip.material': {
            'Meta': {'object_name': 'Material'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clip.product': {
            'Meta': {'object_name': 'Product'},
            'formula': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'window': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Window']"})
        },
        u'clip.producttrim': {
            'Meta': {'object_name': 'ProductTrim'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Material']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Product']"}),
            'trim_length': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '3'}),
            'window': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clip.Window']"})
        },
        u'clip.window': {
            'Meta': {'object_name': 'Window'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['clip']