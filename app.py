import numpy as np
from flask import Flask, render_template,request
import tensorflow as tf

app = Flask(__name__)


def get_prediction(material):
    model = tf.keras.models.load_model(r"C:\Users\anast\OneDrive\Рабочий стол\МГТУ\flask-app\models\material_mlp")
    y_pred = model.predict(material)

    return f"Прогнозируемое соотношение матрица-наполнитель {y_pred}"

@app.route('/')
def index():
    return "main"

@app.route('/predict/',methods=['POST', 'get'])
def processing():
    message = ''
    if request.method == 'POST':
        material = request.form.get('mat')

        material_parameters = material.split(" ")
        material = [float(param) for param in material_parameters]
        material = np.array([material])

        message = get_prediction(material)

    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run()