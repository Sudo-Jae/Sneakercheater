from flask import Flask, render_template, request, jsonify
import requests
import paypalrestsdk

app = Flask(__name__)

paypalrestsdk.configure({
    'mode': 'sandbox',
    'client_id': 'your_paypal_client_id',
    'client_secret': 'your_paypal_client_secret'
})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def app_page():
    return render_template('app.html')

@app.route('/payment', methods=['POST'])
def payment():
    payment = paypalrestsdk.Payment({
        'intent': 'sale',
        'payer': {
            'payment_method': 'paypal'
        },
        'transactions': [{
            'amount': {
                'total': '10.00',
                'currency': 'USD'
            },
            'description': 'SneakerCheater App Usage Fee'
        }],
        'redirect_urls': {
            'return_url': 'http://localhost:5000/payment/success',
            'cancel_url': 'http://localhost:5000/payment/cancel'
        }
    })
    if payment.create():
        return jsonify({"message": "Payment created successfully!"})
    else:
        return jsonify({"message": "Payment creation failed!"})

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
