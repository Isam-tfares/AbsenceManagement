from flask import Flask, request, jsonify
from utils import *

app = Flask(__name__)

@app.route('/identify_person', methods=["POST"])
def identify_person():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    if not '.' in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({'error': 'Invalid file format'})

    try:
        result = identify_person_from_image(file)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

# Problem existed is storage of image uploaded in folder dataset and in FB Storage
@app.route('/add_person', methods=["POST"])
def add_person():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    if 'name' not in request.form:
        return jsonify({'error': 'Name not provided'})

    file = request.files['file']
    name = request.form['name']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    if not '.' in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({'error': 'Invalid file format'})

    try:
        ret = add_user(name, file)
        if ret:
            return jsonify({"success": "User added successfully"})
        else:
            return jsonify({"error": "Failed to add user. Name may already exist."})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)