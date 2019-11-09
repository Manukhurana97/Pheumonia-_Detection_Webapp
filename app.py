from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from keras.preprocessing.image import image
from keras.applications.inception_v3 import preprocess_input
# from keras.applications.vgg16 import preprocess_input
from keras.models import load_model
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


# predict image
def predict_image(path, model):
    #  loading image
    img1 = image.load_img(path, target_size=(224, 224))

    #  image convert to array
    img = image.img_to_array(img1)
    img = np.expand_dims(img, axis=0)

    #  preprocessing image
    img = preprocess_input(img)
    pred = model.predict(img)
    print(pred)
    return pred


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    # load model
    # m = load_model('chest_xrayPneumonia_model.h5')
    m = load_model('chest_xrayInceptionV3')

    if request.method == 'POST':

        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, './uploads', secure_filename(f.filename))
        f.save(file_path)

        score = predict_image(file_path, m)

        if score[0][0] > score[0][1]:
            result = "Congratulation You Don't have Pneumonia"
            p1 = str(score[0][0])
            print(p1)
        else:
            result = "Sorry , You have Pneumonia. \nPlease consult Doctor as soon as"
            p1 = str(score[0][1])
            print(p1)

        return result, p1
    return None


if __name__ == '__main__':
    app.run(debug=True)
