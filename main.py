#Fabiha Ahmed, Kristin Lin
#SoftDev pd09
#Work08 -- login 2.0
#2017-10-08

from flask import Flask, render_template, request, session, redirect, url_for, flash
import os

form = Flask(__name__)

form.secret_key = os.urandom(8)


@form.route('/', methods = ['POST', 'GET'])
def root():
    if 'usr' in session:
        return redirect(url_for('welcome'))
    else:
        return render_template("root.html")

@form.route('/welcome')
def welcome():
    #are you logged in already?
    if 'usr' in session:
        return render_template("result.html", usr = session['usr'])
    else:
        return redirect(url_for('root'))

    
#authorization
#Correct username: softdev
#Correct password: pd09
@form.route('/auth', methods = ['POST'])
def auth():
    usr = request.form["usr"]
    pwd = request.form["pwd"]
    #If username and password are correct, then results
    if usr == 'softdev' and pwd == 'pd09':
        session['usr'] = usr
        flash(session['usr'] + ' has succesfully logged in.')
        return redirect(url_for('welcome'))
    #flash error msgs
    else:
        if not usr == 'softdev' :
            flash('Invalid username')
        if not pwd == 'pd09' :
            flash('Incorrect password')
        return redirect(url_for('root'))    
    
#logout route
@form.route('/logout', methods = ['POST', 'GET'])
def logout():
    flash(session['usr'] + ' has logged out.')
    session.pop('usr') #end session    
    return redirect(url_for("root"))#brings us back to root page
    
if __name__ == "__main__":
    form.debug = True
    form.run()
