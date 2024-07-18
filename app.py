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

@app.route('/ISO27001')
def ISO27001():
    return render_template('individual_certs/ISO27001.html')

@app.route('/ISO27001_checklist')
def ISO27001_checklist():
    return render_template('iso27001/ISO27001_checklist.html')

@app.route('/soc1_type1_checklist')
def soc1_type1_checklist():
    return render_template('/SOC1/soc1_type1.html')

@app.route('/soc1_type2_checklist')
def soc1_type2_checklist():
    return render_template('/SOC1/soc1_type2.html')

if __name__ == '__main__':
    app.run(debug=True)