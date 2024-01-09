from flask import Flask, render_template

app = Flask(__name__)

List = [
   {
      "name": "John Doe",  # fighter's name
      "age": '28',
      "weight": '170',       # Weight in pounds
      "technique": "Muay Thai",
      "reach": '72.5'        # Reach in inches
  },
  {
      "name": "Joydeep",  # fighter's name
      "age": '21',
      "weight": '165',       # Weight in pounds
      "technique": "Striking",
      "reach": '70.5'        # Reach in inches
  }

]




@app.route("/")
def hey():
  return render_template('home.html',
                        fighters=List)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
