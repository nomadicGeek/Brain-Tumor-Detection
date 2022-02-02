from flask import Flask, render_template, request
from tensorflow import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['POST'])
def predict():
    result = {1: "Healthy",
              0: "tumor"}
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    model = keras.models.load_model("model.h5")
    img = load_img(image_path, target_size=(150,150))
    x = img_to_array(img)
    plt.imshow(x)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    pred = model.predict(images)
    pred = int(pred)

    return render_template("result.html", path=image_path, pred=pred)














if __name__ == "__main__":
    app.run(debug=True)