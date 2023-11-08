from flask import Flask
import random

app = Flask(__name__)

@app.route('/trucha', methods=['GET'])
def get_route():
    
    # Generate a random integer between 0 and 9
    random_number1 = random.randint(0, 100)
    random_number2 = random.randint(0, 100)

    # Return a string with the random number
    return {
        "message": f"""Recibiste una cachetada con una trucha de {random_number1} cm de largo y {random_number2} cm de ancho"""
    }

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)