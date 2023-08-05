from flask import Flask

app=Flask(__name__)

#this '@' character elements are known as a decorator and is used to #provide advanced functionalities.
@app.route("/")
def helloworld():
  return "hello world"

# we have created the app but not run the app yet
if(__name__=="__main__"):
  app.run(host="0.0.0.0", debug=True)