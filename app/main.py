from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    day = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open('/log/logfile.log','a') as f:
      f.write(day+' : Hello Log '+os.getenv('ENV','dev')+ ' \n')
      f.close()
    return "Hello from Python! - "+day

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6050)
