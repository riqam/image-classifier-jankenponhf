<<<<<<< HEAD
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Inisialisasi model Jankenpon dari Hugging Face
model_path = 'best_model.h5'
classifier = load_model(model_path)

# Fungsi untuk menampilkan gambar dengan judul
def display_image(image_path, title, width=None):
    image = Image.open(image_path)
    st.image(image, caption=title, use_column_width=width)

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

def main():
    st.title("Let's Play Jankenpon ✋👊✌")
    st.subheader("Choose your jankenpon and see the image prediction!")

    # Membuat session state
    if 'state' not in st.session_state:
        st.session_state.state = {
            'image_choice': '',
            'prediction_result': None
        }

    choice = [
        'paper_1.png', 'paper_2.png', 'paper_3.png', 'paper_4.png', 'paper_5.png',
        'rock_1.png', 'rock_2.png', 'rock_3.png', 'rock_4.png', 'rock_5.png',
        'scissors_1.png', 'scissors_2.png', 'scissors_3.png', 'scissors_4.png', 'scissors_5.png'
    ]

    # Meminta user untuk memilih gambar
    image_choice = st.selectbox("Choose your choice:", ['', *choice])

    enter_button, reset_button = st.columns(2)

    if enter_button.button("Enter"):
        if image_choice:
            # Menampilkan gambar yang dipilih oleh user
            col1, col2 = st.columns(2)
            with col1:
                display_image(image_choice, "Your Choice", width=150)

            # Memproses gambar menjadi format yang sesuai untuk model
            img_array = preprocess_image(image_choice)

            # Memprediksi kelas gambar yang dipilih oleh user
            prediction_result = classifier.predict(img_array)
            predicted_class_index = np.argmax(prediction_result)

            # Daftar kelas Jankenpon
            classes = ['paper', 'rock', 'scissors']
            classes_emoji = ['✋ Paper', '👊 Rock', '✌ Scissors']

            # Menampilkan hasil prediksi dan probability
            st.write(f"<h2 style='font-size: 20px;'>Image Prediction Probabilities:</h2>", unsafe_allow_html=True)
            probabilities = prediction_result[0]
            for i, prob in enumerate(probabilities):
                st.text(f"{classes[i]}: {prob:.4f}")

            st.write(f"<h2 style='font-size: 20px;'>Image Prediction Result: {classes_emoji[predicted_class_index]}</h2>", unsafe_allow_html=True)

            # Menentukan kelas untuk menampilkan gambar 'my choice'
            my_choice_class_index = (predicted_class_index + 2) % 3

            # Menampilkan gambar 'my choice'
            with col2:
                display_image(f"{classes[my_choice_class_index]}_1.png", "My Choice", width=150)

            # Memperbarui session state hanya ketika tombol "Enter" ditekan
            st.session_state.state['image_choice'] = image_choice
            st.session_state.state['prediction_result'] = prediction_result

    if reset_button.button("Reset"):
        # Mereset session state
        st.session_state.state = {}
        st.experimental_rerun()

if __name__ == "__main__":
=======
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Inisialisasi model Jankenpon dari Hugging Face
model_path = 'best_model.h5'
classifier = load_model(model_path)

# Fungsi untuk menampilkan gambar dengan judul
def display_image(image_path, title, width=None):
    image = Image.open(image_path)
    st.image(image, caption=title, use_column_width=width)

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

def main():
    st.title("Let's Play Jankenpon ✋👊✌")
    st.subheader("Choose your jankenpon and see the image prediction!")

    # Membuat session state
    if 'state' not in st.session_state:
        st.session_state.state = {
            'image_choice': '',
            'prediction_result': None
        }

    choice = [
        'paper_1.png', 'paper_2.png', 'paper_3.png', 'paper_4.png', 'paper_5.png',
        'rock_1.png', 'rock_2.png', 'rock_3.png', 'rock_4.png', 'rock_5.png',
        'scissors_1.png', 'scissors_2.png', 'scissors_3.png', 'scissors_4.png', 'scissors_5.png'
    ]

    # Meminta user untuk memilih gambar
    image_choice = st.selectbox("Choose your choice:", ['', *choice])

    enter_button, reset_button = st.columns(2)

    if enter_button.button("Enter"):
        if image_choice:
            # Menampilkan gambar yang dipilih oleh user
            col1, col2 = st.columns(2)
            with col1:
                display_image(image_choice, "Your Choice", width=150)

            # Memproses gambar menjadi format yang sesuai untuk model
            img_array = preprocess_image(image_choice)

            # Memprediksi kelas gambar yang dipilih oleh user
            prediction_result = classifier.predict(img_array)
            predicted_class_index = np.argmax(prediction_result)

            # Daftar kelas Jankenpon
            classes = ['paper', 'rock', 'scissors']
            classes_emoji = ['✋ Paper', '👊 Rock', '✌ Scissors']

            # Menampilkan hasil prediksi dan probability
            st.write(f"<h2 style='font-size: 20px;'>Image Prediction Probabilities:</h2>", unsafe_allow_html=True)
            probabilities = prediction_result[0]
            for i, prob in enumerate(probabilities):
                st.text(f"{classes[i]}: {prob:.4f}")

            st.write(f"<h2 style='font-size: 20px;'>Image Prediction Result: {classes_emoji[predicted_class_index]}</h2>", unsafe_allow_html=True)

            # Menentukan kelas untuk menampilkan gambar 'my choice'
            my_choice_class_index = (predicted_class_index + 2) % 3

            # Menampilkan gambar 'my choice'
            with col2:
                display_image(f"{classes[my_choice_class_index]}_1.png", "My Choice", width=150)

            # Memperbarui session state hanya ketika tombol "Enter" ditekan
            st.session_state.state['image_choice'] = image_choice
            st.session_state.state['prediction_result'] = prediction_result

    if reset_button.button("Reset"):
        # Mereset session state
        st.session_state.state = {}
        st.experimental_rerun()

if __name__ == "__main__":
>>>>>>> efcce81a6be7e77d83a9dad80e49a1e780b51823
    main()