from flask import request,render_template,Flask
import csv

app=Flask('__main__')

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
	if request.method =='POST':
		name = request.form['name']
		emailid = request.form['email-id']
		fieldnames = ['name', 'emailid']
		with open('list.csv','w') as inFile:
			writer=csv.DictWriter(inFile, fieldnames=fieldnames)
			writer.writerow({name:'name', emailid:'emailid'})
		return render_template('thank.html')
app.run(port=5002)