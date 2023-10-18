from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    Education = int(request.form.get('Education'))
    ApplicantIncome = int(request.form.get('ApplicantIncome'))
    CoapplicantIncome = float(request.form.get('CoapplicantIncome'))
    LoanAmount = float(request.form.get('LoanAmount'))
    Credit_History = float(request.form.get('Credit_History'))


    # prediction
    result = model.predict(np.array([Education,ApplicantIncome,CoapplicantIncome,LoanAmount,Credit_History]).reshape(1,5))

    if result[0] == 1:
        result = 'Yes'
    else:
        result = 'No'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)