# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Window'
        db.create_table(u'clip_window', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'clip', ['Window'])

        # Adding model 'Material'
        db.create_table(u'clip_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'clip', ['Material'])

        # Adding model 'Product'
        db.create_table(u'clip_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('window', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Window'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('num', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('formula', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'clip', ['Product'])

        # Adding model 'Product_trim'
        db.create_table(u'clip_product_trim', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('window', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Window'])),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Material'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clip.Product'])),
            ('trim_length', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=3)),
        ))
        db.send_create_signal(u'clip', ['Product_trim'])


    def backwards(self, orm):
        # Deleting model 'Window'
        db.delete_table(u'clip_window')

        # Deleting model 'Material'
        db.delete_table(u'clip_material')

        # Deleting model 'Product'
        db.delete_table(u'clip_product')

        # Deleting model 'Product_trim'
        db.delete_table(u'clip_product_trim')


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
        u'clip.product_trim': {
            'Meta': {'object_name': 'Product_trim'},
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