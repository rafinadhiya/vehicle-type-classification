# Import libraries
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Fungsi untuk memuat model
@st.cache_resource
def load_model_file():
    try:
        model = load_model('best_model_mobilenetv2.h5')  # Gunakan nama file model yang diunggah
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Fungsi prediksi
def predict_image(model, image_file, img_size=(224, 224)):
    # Preprocessing gambar
    img = load_img(image_file, target_size=img_size)  # Resize gambar ke ukuran yang diinginkan
    img_array = img_to_array(img) / 255.0  # Normalisasi piksel ke rentang [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch

    # Prediksi menggunakan model
    predictions = model.predict(img_array)

    # Kelas dengan probabilitas tertinggi
    predicted_class = np.argmax(predictions, axis=-1)[0]
    confidence = np.max(predictions)

    return predicted_class, confidence

# Fungsi utama untuk Streamlit
def run():
    st.title("Vehicle Type Classification - MobileNetV2")
    st.subheader("Upload an image to classify the vehicle type using MobileNetV2")

    # Mapping indeks ke nama kelas kendaraan
    class_indices = {
        0: 'Car',
        1: 'Motorcycle',
        2: 'Bus',
        3: 'Truck'
    }

    # Load model
    st.write("Loading model...")
    model = load_model_file()
    if model is None:
        return

    # File uploader untuk gambar
    image_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "png", "jpeg"])
    if image_file:
        # Tampilkan gambar yang diunggah
        st.image(image_file, caption="Uploaded Image", use_column_width=True)

        # Prediksi gambar
        predicted_class, confidence = predict_image(model, image_file)

        # Tampilkan hasil prediksi
        st.write(f"### Predicted Class: **{class_indices[predicted_class]}**")
        st.write(f"### Confidence: **{confidence:.2f}**")

if __name__ == "__main__":
    run()
