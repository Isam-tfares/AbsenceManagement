from utils import *
from flask import Flask,request,jsonify
# image_path = "./testing_dataset/messi.jpg"
# result = identify_person_from_image(image_path)
# print(result)

# print(add_user("Person 1"))

app=Flask(__name__)


@app.route('/identify_person',methods=["POST"])
def identify_person():
        # Check if a file is present in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Check if the file is an allowed format (e.g., PNG, JPEG)
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    if not '.' in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({'error': 'Invalid file format'})

    # identify person and return his name
    return jsonify(identify_person_from_image(file))


@app.route('/add_person',methods=["POST"])
def add_person():
        # Check if a file and name is present in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    if 'name' not in request.form:
        return jsonify({'error': 'Name not existed '})
    
    file = request.files['file']
    name=request.form['name']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Check if the file is an allowed format (e.g., PNG, JPEG)
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    if not '.' in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({'error': 'Invalid file format'})

    # add user in DB
    ret=add_user(name,file)
    return jsonify({"added":ret})

if __name__=="__main__":
    app.run(debug=True)
