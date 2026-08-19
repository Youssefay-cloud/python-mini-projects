from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'millimeter': 1,
        'centimeter': 10,
        'meter': 1000,
        'kilometer': 1e6,
        'inch': 25.4,
        'foot': 304.8,
        'yard': 914.4,
        'mile': 1.609e6
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        'milligram' : 0.001,
        'gram' : 1,
        'kilogram' : 1000 ,
        'pound' : 453.59237
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

@app.route('/length', methods=['GET', 'POST'])
def length():
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_length(value, from_unit, to_unit)
        return render_template('length.html', result=result)
    return render_template('length.html')


@app.route('/weight', methods=['GET', 'POST'])
def weight():
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_weight(value, from_unit, to_unit)
        return render_template('weight.html', result=result)
    return render_template('weight.html')

if __name__ == '__main__':
    app.run(debug=True)
