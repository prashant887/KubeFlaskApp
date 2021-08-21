from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    with open('/log/logfile.log','a') as f:
      f.write('Hello Log \n')
      f.close()
    return "Hello from Python!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6050)
