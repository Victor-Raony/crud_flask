from flask import Flask

app = Flask(__name__)
print('Running 🔥🔥')

@app.route("/")
def hello_world():
  return 'Hello World!'

@app.route("/about")
def about():
  return "Pagina sobre"

if __name__ == "__main__":
  app.run(debug=True)