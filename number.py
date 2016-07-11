import random
import os
from flask import Flask, render_template, request, session, flash, redirect, g

app=Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
	if 'computer_number' not in session:
		session['computer_number'] = random.randrange(0, 101)
		session['is_game_in_progress'] = True
	if request.method == 'POST':
		user_number = int(request.form['user_number'])
		if session['computer_number'] < user_number:
			flash("High") 


		elif session['computer_number'] > user_number:
			flash('Low')
		elif session['computer_number'] == user_number:
			flash('RightNumber')
			session.pop('computer_number')
			session['is_game_in_progress'] = False
	return render_template('index.html')

app.run()
