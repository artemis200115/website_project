from sqlalchemy import create_engine,text

engine = create_engine("mysql+pymysql://iohb0jue5jwg0xnviea1:pscale_pw_WXQA0hTQTPAzHeICfnMZfJ762Leb3iqLJfiPJ0H9R9P@us-west.connect.psdb.cloud/organicmolecules?charset=utf8mb4", connect_args={
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