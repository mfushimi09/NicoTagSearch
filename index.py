from datetime import datetime, timedelta
from flask import Flask, render_template, request
from nico_api import fetch_from_nico
app = Flask(__name__)

#TODO

@app.route('/')
def hello():

    keyword = request.args.get('keyword') if request.args.get('keyword')  else "ボイロ"
    viewCounter = request.args.get('viewCounter') if request.args.get('viewCounter')  else "10000"
    # starttime = (datetime.today() + timedelta(days=-30) ).strftime("%Y-%m-%d") # from this day
    starttime = request.args.get('starttime')
    starttime = (datetime.today() + timedelta(days=-30) ).strftime("%Y-%m-%d") if not starttime else starttime
    q = {'keyword' : keyword,
         'viewCounter': viewCounter,
         'startTime': starttime
    }

    res = fetch_from_nico(q)
    # return name
    # return render_template('index.html', title='flask test', name=name)
    return render_template('index.html', 
        title='NicoTagSearch', 
        keyword=keyword, 
        viewCounter= viewCounter,
        starttime= starttime,
        res=res
    )

@app.route('/good')
def good():
    name = "Good"
    return name

if __name__ == "__main__":
    app.run(debug=True)