from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def understandingRouting():
    return 'I am learning how to route!'  # Return the string 'Hello World!' as a response

@app.route('/hello')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'Dojo!'  # Return the string 'Hello World!' as a response

@app.route('/say/<name>')          # The "@" decorator associates this route with the function immediately following
def flaskSay(name):
    print(name)
    return 'Hello, ' + name + '!'

#@app.route('/repeat/<num>/<word>')          # The "@" decorator associates this route with the function immediately following
#def flaskSay(num, word):
#    print(word)
#    return word * num



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.