from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db


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


@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs= jobs, img=IMAGES)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  
  if not job:
    return "Not Found", 404
  
  return render_template('moleculeinfo.html', 
                         job=job, img = IMAGES)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)