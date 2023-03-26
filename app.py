from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


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
}]

app = Flask(__name__)


@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs= jobs, img=IMAGES)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)