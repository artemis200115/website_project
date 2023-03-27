from sqlalchemy import create_engine,text
import os

dbconnection = os.environ['dbconnection']

engine = create_engine(dbconnection, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
            
        }})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from molecules"))
    results_as_dict = result.mappings().all()
    jobs = []
    for row in results_as_dict:
      jobs.append(row)
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"select * FROM molecules WHERE id = {id}")
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()