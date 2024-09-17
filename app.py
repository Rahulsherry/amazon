from flask import Flask, render_template, request
import pickle
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model (replace 'MOD.pkl' with the path to your actual model file)

reg_model = pickle.load(open('model (1).pkl', 'rb'))



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    Date = request.form.get('Date')
    Open = request.form.get('Open')
    High = float(request.form.get('High'))
    Low = float(request.form.get('Low'))
    Close = float(request.form.get('Close'))
    AdjClose = float(request.form.get('Adj Close'))
    Volume = float(request.form.get('Volume'))

    # Create a DataFrame with the form data to pass into the model
    data = pd.DataFrame({
        'Date': [Date],
        'Open': [Open],
        'High': [High],
        'Low': [Low],
        'Close': [Close],
        'Adj Close': (AdjClose),
        'Volume': [Volume],
    })
    input_data = [[Date, Open, High, Low, Close, AdjClose]]
    prediction = reg_model.predict(input_data)

    # Return the prediction result to the homepage
    return render_template('home.html', prediction=prediction)


# Run the Flask app
if __name__ == '__main__':
    app.run()



