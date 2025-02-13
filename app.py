from flask import Flask, request, jsonify, abort
from flask.templating import render_template
from model import predict
from features import features_list, feature_form_structure
import traceback

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', feature_form_structure=feature_form_structure)

@app.route('/predict', methods=['POST'])
def create_task():
    try:
        if not request.json:
            abort(400, description="No JSON data received")

        print("Received data:", request.json)
        prediction = predict(request.json)
        return jsonify({'done': True, 'prediction': prediction[0]}), 201

    except Exception as e:
        print("Error during prediction:", str(e))
        print(traceback.format_exc())
        return jsonify({'done': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)