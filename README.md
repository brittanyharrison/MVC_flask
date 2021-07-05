# Model-View-Controller(MVC) with Python Flask 

## Structure of a website 
- HTML - < HyperText markup Language>
```html
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>
``` 

- CSS - {Cascading Style Sheets}
```
body {
  background-color: lightblue;
}

h1 {
  color: white;
  text-align: center;
}

p {
  font-family: verdana;
  font-size: 20px;
}
```  

- JS -  Javascript
```
function storeNames() { return arguments; }
// If we execute the following line in the console:
storeNames("Mulder", "Scully", "Alex Kryceck");
// The output will be { '0': 'Mulder', '1': 'Scully', '2': 'Alex Kryceck' }
```

## Bootstrap

## Model-View-Controller(MVC)
1. A user requests to view a page by entering a URL.
2. The **Controller** receives that request.
3. It uses the **Models** to retrieve all of the necessary data, organizes it, and sends it off to the...
4. **View**, which then uses that data to render the final webpage presented to the the user in their browser.
   

![MVC](https://files.realpython.com/media/mvc_diagram_with_routes.e12c5b982ac8.png)

![Flask](https://devopedia.org/images/article/140/9072.1547744489.png)

## Python Flask
- Flask is a python micro-framework
- Flask is used to develop web applications 

### Let's get started

- Step 1: Insall flask 
`pip install flask`

- Step 2: Create `app.py`

- Step 3: Create an object of this class

- Step 4: create a function to link to home/default page and connect to browser.

```python
from flask import Flask

app = Flask(__name__)  # Creating an app instance


#App function to link to home/default page
@app.route("/")  # connect function to our browser, you will see this in browser
def index():
    return "Welcome to Sparta Global!"


@app.route("/welcome/")  # end slash loads cases with and without slash
def welcome():
    return "<h1> This is a the Devops Stream</h>"


# # create a decorator to route traffic to login page and displays 2 messages
@app.route("/login/")
def login():
    return """
    <h1> Login </h1>
    <form>
  <label for="username">Username:</label><br>
  <input type="text" id="username" name="username"><br>
  <label for="pwd">Password:</label><br>
  <input type="password" id="pwd" name="pwd">
</form>
    """
```
