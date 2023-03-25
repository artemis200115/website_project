from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Linalool',
    'family': 'Alcohols',
    'function': 'Lavender'
  },
  {
    'id': 2,
    'title': 'Linalool',
    'family': 'Alcohols',
    'function': 'Lavender'
  },
 {
    'id': 3,
    'title': 'Linalool',
    'family': 'Alcohols',
    'function': 'Lavender'
  },
  {
    'id': 4,
    'title': 'Linalool',
    'family': 'Alcohols',
    'function': 'Lavender'
  }
]


@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs= JOBS)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  
  if not job:
    return "Not Found", 404
  
  return render_template('jobpage.html', 
                         job=job)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)