#from flask import Flask: this imports the Flask class from the flask module.
#Added request to the import statement to recieve information
from flask import Flask, request
# imports the rotate_string function from the caesar file.
from caesar import rotate_string

#app = Flask(__name__): app will be the object created by the constructor Flask. __name__ is a variable controlled by Python that tells code what module it's in.
app = Flask(__name__)
#app.config['DEBUG'] = True: the DEBUG configuration setting for the Flask application will be enabled.
# This enables some behaviors that are helpful when developing Flask apps, such as displaying errors in the browser,
# and ensuring file changes are reloaded while the server is running (aka "host swapping")
app.config['DEBUG'] = True

#This is where I put the HTML form
form_html = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- TO DO: The form uses the POST method. -->
      <form action="/" method="POST">
        <!-- TO DO: There are two inputs: a regular input with type="text" and a textarea. -->
        <!-- TO DO: Has a label on the input element that looks something like the one in the screenshot above. -->
        <label>
            Rotate by:
            <!-- TO DO: Set name="rot" on the input element and name="text" on the textarea -->
            <!-- TO DO: The input element has the default value of 0. -->
            <input type="text" name="rot" value="0"/>
        </label>
        <textarea type="text" name="text">
        </textarea>
        <!-- TO DO: Has a submit button.-->
        <input type="submit" value="Submit"/>
      </form>
    </body>
</html>
"""

#@app.route("/"): this is a decorator that creates a mapping between the path - in this case the root, or "/", and the function that we're about to define
@app.route("/")
#def index():: Ah, familiar ground! We define index, a function of zero variables
def index():
    #return "Hello World": Our function returns a string literal.
    #return "Hello World"
    #return the html form
    return form_html

# Add an @app.route decorator to configure the function to receive requests at the root path "/",
# and with methods=['POST'].
@app.route("/", methods=['POST'])
#To process the form, define a new function encrypt in main.py.
#When the form is submitted, the request will contain the parameters rot and text
def encrypt():
    #Within encrypt, store the values of these request parameters in local variables,
    # converting data types as necessary.
    # Then, encrypt the value of the text parameter using rotate_string.
    # Return the encrypted string wrapped in <h1> tags, to be rendered in the browser.
    rot = request.form['rot']
    text = request.form['text']
    rot = int(rot)
    rotated_string = rotate_string(text, rot)

    return "<h1>" + rotated_string + "</h1>"

#app.run(): Pass control to the Flask object.
# The run function loops forever and never returns, so put it last.
# It carries out the responsibilities of a web server, listening for requests and sending responses over a network connection.
app.run()