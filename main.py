#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import ndb

ResultsCSV = ''

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Pairs(ndb.Model):
  pairId = ndb.IntegerProperty()
  name1 = ndb.StringProperty()
  path1 = ndb.StringProperty()
  name2 = ndb.StringProperty()
  path2 = ndb.StringProperty()
  isSame = ndb.BooleanProperty()  #property to indicate if the record pictures represent the same races 

class MainHandler(webapp.RequestHandler):
  def get (self, q):
    if q is None:
      q = 'index.html'

    pairs = Pairs.query().fetch();  
    template_values = {
	    'pairs': pairs
    }
		
    #path = os.path.join (os.path.dirname (__file__), q)
	
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render(template_values))
    #self.response.headers ['Content-Type'] = 'text/html'
    #self.response.out.write (template.render (path, {}))
	
class GetJsonData(webapp.RequestHandler):	
    def get(self):
		pairs = Pairs.query()
		result = json.dumps([p.to_dict() for p in Pairs.query().fetch()])
		self.response.write(result)

class SetResults(webapp.RequestHandler):	
    def post(self):
		results = self.request.get('pairResults')
		ResultsCSV = results
		
class ReturnResults(webapp.RequestHandler):	
    def get(self):
		#results = self.request.get('data')
		self.response.headers['Content-Type'] = 'text/csv'
		self.response.headers['content-disposition'] = 'attachment; filename=results.csv'
		self.response.write(ResultsCSV)
		
class AddDataStoreManually(webapp.RequestHandler):
	def get(self):
		pairs = Pairs(pairId = 0, name1 = 'appalossa7' ,path1 = 'images/exp/pair_0/horse0.png', name2='appalossa6',path2='images/exp/pair_0/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 1, name1 = 'CrosDorado' ,path1 = 'images/exp/pair_1/horse0.png', name2='AmericanSaddle',path2='images/exp/pair_1/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 2, name1 = 'arabian6' ,path1 = 'images/exp/pair_2/horse0.png', name2='Andalusian',path2='images/exp/pair_2/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 3, name1 = 'Andalusian2' ,path1 = 'images/exp/pair_3/horse0.png', name2='Canadian3',path2='images/exp/pair_3/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 4, name1 = 'Barb' ,path1 = 'images/exp/pair_4/horse0.png', name2='Barb2',path2='images/exp/pair_4/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 5, name1 = 'SugarBush2' ,path1 = 'images/exp/pair_5/horse0.png', name2='SugarBush4',path2='images/exp/pair_5/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 6, name1 = 'Barb3' ,path1 = 'images/exp/pair_6/horse0.png', name2='appalossa8',path2='images/exp/pair_6/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 7, name1 = 'Canadian2' ,path1 = 'images/exp/pair_7/horse0.png', name2='DalesPony',path2='images/exp/pair_7/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 8, name1 = 'Dapple2' ,path1 = 'images/exp/pair_8/horse0.png', name2='Dapple3',path2='images/exp/pair_8/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 9, name1 = 'LeopardSpottedHorse' ,path1 = 'images/exp/pair_9/horse0.png', name2='DalesPony2',path2='images/exp/pair_9/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 10, name1 = 'SugarBush' ,path1 = 'images/exp/pair_10/horse0.png', name2='gypsy',path2='images/exp/pair_10/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 11, name1 = 'Westphalian' ,path1 = 'images/exp/pair_11/horse0.png', name2='Westphalian3',path2='images/exp/pair_11/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 12, name1 = 'Quorter8' ,path1 = 'images/exp/pair_12/horse0.png', name2='Quorter4',path2='images/exp/pair_12/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 13, name1 = 'Irish2' ,path1 = 'images/exp/pair_13/horse0.png', name2='Irish',path2='images/exp/pair_13/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 14, name1 = 'Holland' ,path1 = 'images/exp/pair_14/horse0.png', name2='Holland2',path2='images/exp/pair_14/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 15, name1 = 'Thoroughbred5' ,path1 = 'images/exp/pair_15/horse0.png', name2='palomino',path2='images/exp/pair_15/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 16, name1 = 'Paint10' ,path1 = 'images/exp/pair_16/horse0.png', name2='Paint9',path2='images/exp/pair_16/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 17, name1 = 'RockeyMountain' ,path1 = 'images/exp/pair_17/horse0.png', name2='Quorter7',path2='images/exp/pair_17/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 18, name1 = 'Turkoman' ,path1 = 'images/exp/pair_18/horse0.png', name2='Westphalian2',path2='images/exp/pair_18/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 19, name1 = 'Buckskin4' ,path1 = 'images/exp/pair_19/horse0.png', name2='Buckskin2',path2='images/exp/pair_19/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 20, name1 = 'Thoroughbred' ,path1 = 'images/exp/pair_20/horse0.png', name2='Mustang',path2='images/exp/pair_20/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 21, name1 = 'Dapple' ,path1 = 'images/exp/pair_21/horse0.png', name2='Arabian5',path2='images/exp/pair_21/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 22, name1 = 'Buckskin3' ,path1 = 'images/exp/pair_22/horse0.png', name2='palomino2',path2='images/exp/pair_22/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 23, name1 = 'WelshPony5' ,path1 = 'images/exp/pair_23/horse0.png', name2='WelshPony6',path2='images/exp/pair_23/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 24, name1 = 'Australian2' ,path1 = 'images/exp/pair_24/horse0.png', name2='Australian',path2='images/exp/pair_24/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 25, name1 = 'Holsteiner' ,path1 = 'images/exp/pair_25/horse0.png', name2='FriesianPony',path2='images/exp/pair_25/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 26, name1 = 'Paint8' ,path1 = 'images/exp/pair_26/horse0.png', name2='Paint7',path2='images/exp/pair_26/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 27, name1 = 'Shire6' ,path1 = 'images/exp/pair_27/horse0.png', name2='Shire5',path2='images/exp/pair_27/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 28, name1 = 'silesian' ,path1 = 'images/exp/pair_28/horse0.png', name2='Paint11',path2='images/exp/pair_28/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 29, name1 = 'FjordPony2' ,path1 = 'images/exp/pair_29/horse0.png', name2='FjordPony',path2='images/exp/pair_29/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 30, name1 = 'Arabian1' ,path1 = 'images/exp/pair_30/horse0.png', name2='missouri1',path2='images/exp/pair_30/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 31, name1 = 'friesian1' ,path1 = 'images/exp/pair_31/horse0.png', name2='Tennessee6',path2='images/exp/pair_31/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 32, name1 = 'Paint5' ,path1 = 'images/exp/pair_32/horse0.png', name2='appallosa1',path2='images/exp/pair_32/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 33, name1 = 'appallosa2' ,path1 = 'images/exp/pair_33/horse0.png', name2='appallosa3',path2='images/exp/pair_33/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 34, name1 = 'Paint6' ,path1 = 'images/exp/pair_34/horse0.png', name2='appallosa4',path2='images/exp/pair_34/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 35, name1 = 'Paint3' ,path1 = 'images/exp/pair_35/horse0.png', name2='Paint1',path2='images/exp/pair_35/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 36, name1 = 'Paint4' ,path1 = 'images/exp/pair_36/horse0.png', name2='Paint2',path2='images/exp/pair_36/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 37, name1 = 'Quorter6' ,path1 = 'images/exp/pair_37/horse0.png', name2='appallosa5',path2='images/exp/pair_37/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 38, name1 = 'shire4' ,path1 = 'images/exp/pair_38/horse0.png', name2='shire1',path2='images/exp/pair_38/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 39, name1 = 'belgian_horse1' ,path1 = 'images/exp/pair_39/horse0.png', name2='belgian_horse2',path2='images/exp/pair_39/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 40, name1 = 'hanover3' ,path1 = 'images/exp/pair_40/horse0.png', name2='friesian2',path2='images/exp/pair_40/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 41, name1 = 'friesian3' ,path1 = 'images/exp/pair_41/horse0.png', name2='friesian4',path2='images/exp/pair_41/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 42, name1 = 'tennessee4' ,path1 = 'images/exp/pair_42/horse0.png', name2='hanover1',path2='images/exp/pair_42/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 43, name1 = 'WelshPony1' ,path1 = 'images/exp/pair_43/horse0.png', name2='WelshPony4',path2='images/exp/pair_43/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 44, name1 = 'hanover2' ,path1 = 'images/exp/pair_44/horse0.png', name2='arabian2',path2='images/exp/pair_44/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 45, name1 = 'belgian_horse3' ,path1 = 'images/exp/pair_45/horse0.png', name2='belgian_horse4',path2='images/exp/pair_45/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 46, name1 = 'WelshPony2' ,path1 = 'images/exp/pair_46/horse0.png', name2='tennessee3',path2='images/exp/pair_46/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 47, name1 = 'quorter2' ,path1 = 'images/exp/pair_47/horse0.png', name2='quorter1',path2='images/exp/pair_47/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 48, name1 = 'suffolk1' ,path1 = 'images/exp/pair_48/horse0.png', name2='shetland_pony3',path2='images/exp/pair_48/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 49, name1 = 'Arabian4' ,path1 = 'images/exp/pair_49/horse0.png', name2='thoroughbred2',path2='images/exp/pair_49/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 50, name1 = 'quorter5' ,path1 = 'images/exp/pair_50/horse0.png', name2='quorter3',path2='images/exp/pair_50/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 51, name1 = 'Shire2' ,path1 = 'images/exp/pair_51/horse0.png', name2='Shire3',path2='images/exp/pair_51/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 52, name1 = 'welsh_pony3' ,path1 = 'images/exp/pair_52/horse0.png', name2='thoroughbred3',path2='images/exp/pair_52/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 53, name1 = 'norwayFjordPony2' ,path1 = 'images/exp/pair_53/horse0.png', name2='missouri3',path2='images/exp/pair_53/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 54, name1 = 'suffolk2' ,path1 = 'images/exp/pair_54/horse0.png', name2='suffolk3',path2='images/exp/pair_54/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 55, name1 = 'shetland_pony2' ,path1 = 'images/exp/pair_55/horse0.png', name2='shetland_pony1',path2='images/exp/pair_55/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 56, name1 = 'tennessee1' ,path1 = 'images/exp/pair_56/horse0.png', name2='tennessee2',path2='images/exp/pair_56/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 57, name1 = 'thoroughbred1' ,path1 = 'images/exp/pair_57/horse0.png', name2='thoroughbred4',path2='images/exp/pair_57/horse1.png',isSame=True)	
		pairs.put()
		pairs = Pairs(pairId = 58, name1 = 'Arabian3' ,path1 = 'images/exp/pair_58/horse0.png', name2='hanover4',path2='images/exp/pair_58/horse1.png',isSame=False)	
		pairs.put()
		pairs = Pairs(pairId = 59, name1 = 'haflinger' ,path1 = 'images/exp/pair_59/horse0.png', name2='NorwayFjordPony1',path2='images/exp/pair_59/horse1.png',isSame=False)	
		pairs.put()		
		
		
		
application = webapp.WSGIApplication ([
	('/(.*html)?', MainHandler),
	('/GetJsonData', GetJsonData),
	('/SetResults', SetResults),
	('/ReturnResults', ReturnResults),
	('/AddDataStoreManually', AddDataStoreManually)
], debug=True)
util.run_wsgi_app (application)

if __name__ == '__main__':
  main ()
