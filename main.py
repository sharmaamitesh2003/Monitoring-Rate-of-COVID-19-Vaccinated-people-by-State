import bottle
import json
import data
import processing
@bottle.route("/")
def html_provider():
 return bottle.static_file("index.html", root=".")

@bottle.route("/bar")
def barGraph_requested():
  data1 = data.load_data("saved_data.csv")
  date1 = processing.max_value(data1, 'date')
  acc = []
  for dict1 in data1:
   if date1 == dict1["date"]:
      acc.append(dict1)
  data2 = data.make_lists(["location", "series_complete_pop_pct"], acc)
  return json.dumps(data2)

@bottle.route("/script.js")
def js_provider():
  return bottle.static_file("script.js", root=".")

@bottle.route("/pie")
def pieGraph_requested():
  data1 = data.load_data("saved_data.csv")
  acc1 = []
  for dict1 in data1:
   data2 = data.make_values_numeric(['administered_moderna', 'administered_pfizer', 'administered_janssen', 'administered_unk_manuf'], dict1)
   acc1.append(data2)
  data3 = data.make_lists(['administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf'], acc1)
  return json.dumps(data3)
# @bottle.route("/linebar")
# def data_line():

@bottle.post("/line")
def lineGraph_data():
  json_receive = bottle.request.body.read().decode()
  response2 = json.loads(json_receive)
  data1 = data.load_data("saved_data.csv")
  acc = []
  for dict in data1:
   if "2021" in dict["date"] and response2 == dict["location"]:
    acc.append(dict)
  data2 = data.make_lists(["date","location", "series_complete_pop_pct"],acc)
  return json.dumps(data2)
import os.path
def load_data():
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
   url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
   info = data.json_loader(url)
   heads =['date','location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
   data.save_data(heads, info, 'saved_data.csv')
load_data()
bottle.run(host="0.0.0.0",post=8080, debug=True)
