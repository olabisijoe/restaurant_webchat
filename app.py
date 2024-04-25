from re import A
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = {
    "hello": ["Hi there! Welcome to Yummychops food and catering services, My name is Naomi, your digital Yummychops assistant. What would you like to order?"],
"special fried rice and barbecue chicken": ["Got it,  would you like to add any more items to your order?"],

"what is on your drink menu?": ["we have a variety of soda drinks, fritzy drinks, diary drinks, fresh juices and smoothies"],

"i want 3 cans of banana and apple smoothie": ["Great choice!, anything else you would like?"],

"nothing else": ["please send us your name, contact address and phone number using +2347035345636 for your delivery"],

"i want to order": ["please send us your name, contact address and phone number using +2347035345636 for your delivery"],

"how long until I get my order?": ["it would only take the rider 20mins to get to you"],

"one more thing": ["Sure! go ahead please"],

"when are your opening hours?": ["We're open from 9am to 10pm every day, Join us whenever you're hungry!"],

"can I make a reservation?": ["Certainly! You can make a reservation on our website or call us on +2347035345636 "],

"are you serious": ["I'm sorry, I'm not sure how to respond to that"],

"thank you for your assistance": ["it's my pleasure!"],

"bye": ["Take care!"],
    }

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"].lower()
    
    if user_input in responses:
        response = random.choice(responses[user_input])
    else:
        response = "I'm a simple chatbot. I don't understand that."

    return jsonify({"response": response})

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')


if __name__ == "__main__":
    app.run(debug=True)
