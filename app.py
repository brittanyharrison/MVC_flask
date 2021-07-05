from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)  # Creating an app instance


#App function to link to home/default page
@app.route("/")  # connect function to our browser, you will see this in browser
def index():
    return "Welcome to Sparta Global!"


@app.route("/welcome/")  # end slash loads cases with and without slash
def welcome():
    return render_template("welcome.html")


# # create a decorator to route traffic to login page and displays 2 messages
@app.route("/login/")
def login():
#     return """
#     <h1> Login </h1>
#     <form>
#   <label for="username">Username:</label><br>
#   <input type="text" id="username" name="username"><br>
#   <label for="pwd">Password:</label><br>
#   <input type="password" id="pwd" name="pwd">
# </form>
#     """
    return redirect(url_for("welcome"))  # Redirect the users if they visit login page


if __name__ == "__main__":
    app.run(debug=True)

