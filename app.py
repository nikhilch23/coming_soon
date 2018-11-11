from flask import request,render_template,Flask, redirect, url_for
import csv

app=Flask('__main__')

@app.route('/')
def main():
	return render_template('index.html')

row = ['Name','Email']

with open('list.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(row)

@app.route('/submit', methods = ['GET','POST'])
def submit():
	if request.method =='POST':
		name = request.form['name']
		emailid = request.form['email-id']
		fieldnames = [name,emailid]
		with open('list.csv','a') as inFile:
			writer=csv.writer(inFile)
			writer.writerow(fieldnames)
	
	return render_template('thank.html')

app.run(port=5002)