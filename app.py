from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/SOC1')
def soc1():
    return render_template('individual_certs/SOC1.html')

@app.route('/GDPR')
def GDPR():
    return render_template('individual_certs/GDPR.html')

if __name__ == '__main__':
    app.run(debug=True)