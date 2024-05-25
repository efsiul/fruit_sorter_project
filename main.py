from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
import pickle
import base64
import io
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


class KerasModelLoader:
    def __init__(self, filename):
        self.filename = filename

    def load_model(self):
        with open(self.filename, 'rb') as f:
            return pickle.load(f)

def load_models():
    model_paths = [
        "models/inceptionv3.pkl",
        "models/inceptionv3-2.pkl",
        "models/vgg16.pkl",
        "models/vgg16_2.pkl",
        "models/densenet121.pkl",
        "models/resnet50.pkl",
        "models/mobilNet.pkl"
    ]

    models = []
    for path in model_paths:
        with open(path, "rb") as file:
            model = pickle.load(file)
            # Extraer el nombre del modelo del nombre del archivo
            model_name = os.path.basename(path).split(".")[0]
            models.append((model_name, model))
    return models

class_labels = {
    0: "freshapples",
    1: "freshbanana",
    2: "freshoranges",
    3: "rottenapples",
    4: "rottenbanana",
    5: "rottenoranges"
}

# Función para predecir usando los modelos cargados
def predict_with_models(models, image_array):
    predictions = []
    for model_name, model in models:
        prediction = model.predict(image_array)
        max_index = np.argmax(prediction)
        max_probability = float(np.max(prediction))
        # Obtener el nombre de la etiqueta correspondiente al índice predicho
        predicted_label = class_labels[max_index]
        predictions.append({
            "Nombre del Modelo": model_name,
            "Resultado de la clasificación": predicted_label,
            "Probabilidad del resultado": max_probability,
        })
    return predictions

# Cargar los modelos al inicio de la aplicación
models = load_models()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    image = image.resize((224, 224))  # Ajustar tamaño según sea necesario
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    predictions = predict_with_models(models, image_array)

    # Convertir la imagen a base64 para incluirla en la respuesta
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='JPEG')
    img_byte_array = img_byte_array.getvalue()
    img_base64 = base64.b64encode(img_byte_array).decode()

    # Renderizar la plantilla HTML con las predicciones y la imagen
    return templates.TemplateResponse("result.html", {"request": {}, "predictions": predictions, "image": img_base64})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
