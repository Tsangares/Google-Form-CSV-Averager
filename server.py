from flask import Flask,request,redirect,render_template,send_file
from util import extractAverages
import time,sys,os
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stats', methods=['POST'])
def stats():
    csv=request.files['csv']
    numerical=extractAverages(str(csv.read()))
    return render_template('stats.html', numerical=numerical)

if __name__=='__main__':
    app.run('0.0.0.0', port=6065,debug=True)
