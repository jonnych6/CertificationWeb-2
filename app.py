from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/toc')
def toc():
    return render_template('toc.html')

### home page per certification
@app.route('/SOC1')
def soc1():
    return render_template('individual_certs/SOC1.html')

@app.route('/SOC2')
def soc2():
    return render_template('individual_certs/SOC2.html')

@app.route('/SOC3')
def soc3():
    return render_template('individual_certs/SOC3.html')

@app.route('/GDPR')
def GDPR():
    return render_template('individual_certs/GDPR.html')

@app.route('/PCI')
def PCI():
    return render_template('individual_certs/PCI_DSS.html')

@app.route('/ISO27001')
def ISO27001():
    return render_template('individual_certs/ISO27001.html')

@app.route('/GRC')
def GRC():
    return render_template('individual_certs/GRC.html')

@app.route('/HIPAA')
def HIPAA():
    return render_template('individual_certs/HIPAA.html')

### end off home page per certification

###checklist routes per certification   

@app.route('/PCI_DSS_checklist')
def PCI_DSS_checklist():
    return render_template('/PCI_DSS/PCI_DSS_checklist.html')

@app.route('/GRC_checklist')
def GRC_checklist():
    return render_template('/GRC/GRC_checklist.html')

@app.route('/GDPR_checklist')
def GDPR_checklist():
    return render_template('/GDPR/GDPR_checklist.html')

@app.route('/ISO27001_checklist')
def ISO27001_checklist():
    return render_template('iso27001/ISO27001_checklist.html')

@app.route('/soc1_type1_checklist')
def soc1_type1_checklist():
    return render_template('/SOCx/soc1_type1.html')

@app.route('/soc1_type2_checklist')
def soc1_type2_checklist():
    return render_template('/SOCx/soc1_type2.html')

@app.route('/soc2_type1_checklist')
def soc2_type1_checklist():
    return render_template('/SOCx/soc2_type1_checklist.html')

@app.route('/soc2_type2_checklist')
def soc2_type2_checklist():
    return render_template('/SOCx/soc2_type2_checklist.html')

@app.route('/soc3_checklist')
def soc3_checklist():
    return render_template('/SOCx/soc3_checklist.html')

### end of checklist routes per certification


## SOC comparison routes
@app.route('/comp_soc1_soc2')
def comp_soc1_soc2():
    return render_template('/SOCx/comp_soc1_soc2.html')

@app.route('/comp_soc1_soc3')
def comp_soc1_soc3():
    return render_template('/SOCx/comp_soc1_soc3.html')

@app.route('/comp_soc_all')
def comp_soc_all():
    return render_template('/SOCx/comp_soc_all.html')

if __name__ == '__main__':
    app.run(debug=True)