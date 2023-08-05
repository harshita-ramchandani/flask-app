from flask import Flask, render_template

app=Flask(__name__)
# making changes again and in a html file are tricky, therefore we makechanges in a database and the data is taken from the database and displayed on the html page. 
#this '@' character elements are known as a decorator and is used to #provide advanced functionalities.
JOBS=[
  {
    'id':1,
    'job': "data analyst",
    'location':"bengaluru",
    'salary':"1,00,000"
  },
  {
    'id':2,
    'job': "data scientist",
    'location':"chennai",
    'salary':"1,00,000"
  },
  {
    'id':3,
    'job': "backened engineer",
    'location':"chennai",
    'salary':"1,00,000"
  }
]
@app.route("/")
def helloworld():
  return render_template('home.html',jobs=JOBS)

# we have created the app but not run the app yet
if(__name__=="__main__"):
  app.run(host="0.0.0.0", debug=True)