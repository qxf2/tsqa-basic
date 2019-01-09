"""
This is a Flask application that can be used to calculate the BMI of the user. 

"""

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def calculate_bmi(user_weight,user_height):
    "Calaculate the user BMI"
    bmi_of_the_user = int(user_weight/(user_height*user_height))

    return bmi_of_the_user

@app.route("/", methods=['GET', 'POST'])
@app.route("/bmicalculator", methods=['GET', 'POST'])
def bmicalculator():
    "Endpoint for calculating the BMI of the user"
    if request.method == 'GET':
        #return the form
        return render_template('index.html')
    if request.method == 'POST':
        #return the answer
        user_weight = int(request.form.get('userweight'))
        user_height = float(request.form.get('userheight'))
        user_bmi = calculate_bmi(user_weight,user_height)
        api_response = {"user_bmi":user_bmi}
        return jsonify(api_response)

#---START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug= True)