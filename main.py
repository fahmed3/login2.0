#Fabiha Ahmed, Kristin Lin
#SoftDev pd09
#Work08 -- login 2.0
#2017-10-08

from flask import Flask, render_template, request, session, redirect, url_for
import os

form = Flask(__name__)

form.secret_key = os.urandom(8)


@form.route('/', methods = ['POST', 'GET'])
def root():
    if 'usr' in session:
        return redirect(url_for('requests')) #welcome page
    else:
        return render_template("root.html")

#Correct username: softdev
#Correct password: pd09
@form.route('/result', methods = ['POST', 'GET'])
def requests():
    #are you logged in already?
    if 'usr' in session:
        return render_template("result.html", usr = session['usr'])
    #either POST or GET method
    if request.method == 'POST':
        usr = request.form["usr"]
        pwd = request.form["pwd"]
    else:
        usr = request.args['usr']
        pwd = request.args['pwd']
    #If username and password are correct, then results
    if usr == 'softdev' and pwd == 'pd09':
        session['usr'] = usr
        return render_template("result.html", usr = usr)
    #else send to error page, with booleans for password and username
    else:
        return render_template("error.html", cUsr = (usr == 'softdev'),
        cPwd = (pwd == 'pd09'))

#logout route
@form.route('/logout', methods = ['POST', 'GET'])
def logout():
    session.pop('usr') #end session
    return redirect(url_for("root"))#brings us back to root page
    
if __name__ == "__main__":
    form.debug = True
    form.run()
