#imports 

from flask import Flask, render_template, jsonify
from database import load_molecules, load_molecule

#image database stored locally

IMAGES =[ {

'id':1,
'link': 'https://websiteproject.tacogguk.repl.co/static/penicillin.png'
}, {

'id':2,
'link': 'https://websiteproject.tacogguk.repl.co/static/ddt.png'
}, 
        {

'id':3,
'link': 'https://websiteproject.tacogguk.repl.co/static/morphine.png'
}, 
        {

'id':4,
'link': 'https://websiteproject.tacogguk.repl.co/static/octanitrocubane.png'
}, 
        {

'id':5,
'link': 'https://websiteproject.tacogguk.repl.co/static/bullvalene.png'
}, 
         {

'id':6,
'link': 'https://websiteproject.tacogguk.repl.co/static/indigo.png'
}]

app = Flask(__name__)


#loading molecule info on home page of website 
#molecule website stored in mysql database

@app.route("/")
def load_webpage():
    molecules = load_molecules()
    return render_template('home.html', 
                          molecules= molecules, img=IMAGES)

#loading molecule info on individual pages of website

@app.route("/molecule/<id>")
def show_molecule(id):
  molecule = load_molecule(id)
  
  if not molecule:
    return "Not Found", 404
  
  return render_template('moleculeinfo.html', 
                         molecule=molecule, img = IMAGES)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)