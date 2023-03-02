from flask import Flask, render_template

app = Flask(__name__)

#Dice Main page
@app.route('/')
def dice_page():
	return render_template('dice_page.html')

#Testing to check if it works
@app.route('/test')
def test():
    return "Works!"