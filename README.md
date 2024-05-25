# **Modelo de Detección de Frutas Frescas con Red Neuronal Convolucional VGG16**

Este proyecto es un modelo de clasificación de imágenes de frutas utilizando modelos de aprendizaje automático. Puedes lanzar y ejecutar fácilmente este proyecto utilizando Docker.

## Instrucciones de cómo lanzar el proyecto con Docker

1. Asegúrate de tener Docker instalado en tu sistema.
2. Clona este repositorio en tu máquina local.
3. Dirigete a la siguiente dirección <https://drive.google.com/drive/folders/10x6oecGwCxZyPOVjk7FTFcyOry6sIazr?usp=drive_link>
4. Es una dirección de drive donde encontraras los 7 modelos que se deben pegar en la carpeta models en tu proyecto local
5. La carpeta tiene acceso restringido por ser empresarial, para más información comunicarse felipe.cadavid@udea.edu.co
6. Abre una terminal y navega hasta el directorio raíz del proyecto.
7. Ejecuta el siguiente comando para construir y lanzar el contenedor Docker:

    ```bash
        docker-compose up --build
    ```

8. Una vez que el contenedor esté en funcionamiento, podrás acceder a la aplicación en tu navegador web en la dirección <http://localhost:8000>.

---

## Estructura del proyecto

El proyecto está estructurado de la siguiente manera:

```bash
    models/
    │   ├── densenet121.pkl
    │   ├── inceptionv3-2.pkl
    │   ├── inceptionv3.pkl
    │   ├── mobilNet.pkl
    │   ├── resnet50.pkl
    │   ├── vgg16_2.pkl
    │   └── vgg16.pkl
    templates/
    │   └── index.html
    docker-compose.yml
    Dcokerfile
    main.py
    README.md
    requirements.txt
```

* **models/**: Contiene los archivos de los modelos de aprendizaje automático utilizados para la clasificación de frutas.
* **main.py**: El archivo principal que contiene el código para el servidor FastAPI y la lógica de clasificación de imágenes.
* **templates/**: Contiene los archivos HTML utilizados para la interfaz de usuario.
* **requirements.txt**: Archivo que especifica las dependencias del proyecto.

---

## Información de los modelos

El proyecto utiliza los siguientes modelos de aprendizaje automático para la clasificación de frutas:

1. **DenseNet121:** Modelo de red neuronal convolucional profunda utilizado para tareas de clasificación de imágenes.
2. **InceptionV3:** Arquitectura de red neuronal convolucional diseñada para el reconocimiento de imágenes.
3. **MobileNet:** Arquitectura de red neuronal convolucional ligera diseñada para su uso en dispositivos móviles y sistemas con recursos limitados.
4. **ResNet50:** Modelo de red neuronal convolucional profunda que ha demostrado un rendimiento excepcional en tareas de clasificación de imágenes.
5. **VGG16:** Modelo de red neuronal convolucional desarrollado por Visual Geometry Group en la Universidad de Oxford, ampliamente utilizado en tareas de clasificación de imágenes.

Estos modelos están pre-entrenados en conjuntos de datos de imágenes y se utilizan para predecir las clases de frutas en las imágenes de entrada.
