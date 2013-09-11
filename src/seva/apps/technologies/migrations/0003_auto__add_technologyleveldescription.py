# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TechnologyLevelDescription'
        db.create_table(u'technologies_technologyleveldescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('technology', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['technologies.Technology'])),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'technologies', ['TechnologyLevelDescription'])


    def backwards(self, orm):
        # Deleting model 'TechnologyLevelDescription'
        db.delete_table(u'technologies_technologyleveldescription')


    models = {
        u'technologies.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'technologies.technology': {
            'Meta': {'object_name': 'Technology'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['technologies.Category']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'technologies.technologyleveldescription': {
            'Meta': {'object_name': 'TechnologyLevelDescription'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'technology': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['technologies.Technology']"})
        }
    }

    complete_apps = ['technologies']