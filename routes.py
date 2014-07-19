from flask import Flask, render_template, request
import urllib2
import json

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=('GET', 'POST'))
def submit():
        if request.form['convert'] == 'convert':
            response = urllib2.urlopen('http://www.cryptocoincharts.info/v2/api/tradingPair/BTC_USD')
            http = response.read()
            j = json.loads(http)
            bitstamp = j['price']
            if request.form['select'] == 'btc2usd':
                btc = request.form['BTC']
                conversion = float(btc) * float(bitstamp)
                return render_template('conversion.html', bitstamp=bitstamp, btc=btc, conversion=conversion)
            else:
                btc = request.form['BTC']
                conversion = float(btc) * (1/float(bitstamp))
                return render_template('conversion1.html', bitstamp=bitstamp, btc=btc, conversion=conversion)
        if request.form['convert'] == 'home':
            return render_template('index.html')

@app.route('/reset', methods=('GET', 'POST'))
def reset():
    if request.form['Reset'] == 'Reset':
        response = urllib2.urlopen('http://www.cryptocoincharts.info/v2/api/tradingPair/BTC_USD')
        http = response.read()
        j = json.loads(http)
        bitstamp = j['price']
        return render_template('home.html', bitstamp=bitstamp)
    else:
         return render_template('index.html')

@app.route('/appy', methods=('GET', 'POST'))
def appy():
    response = urllib2.urlopen('http://www.cryptocoincharts.info/v2/api/tradingPair/BTC_USD')
    http = response.read()
    j = json.loads(http)
    bitstamp = j['price']
    return render_template('home.html', bitstamp=bitstamp)

@app.route('/stocktrak', methods=('GET', 'POST'))
def stocktrak():
    return render_template('stocktrak.html')

@app.route('/about', methods=('GET', 'POST'))
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run()