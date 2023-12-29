# Import libraries
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Initialize the Jankenpon model from Hugging Face
model_path = 'best_model.h5'
classifier = load_model(model_path)

# Function to display images with titles
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

    # Create the session state
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

    # Asks the user to select an image
    image_choice = st.selectbox("Choose your choice:", ['', *choice])

    enter_button, reset_button = st.columns(2)

    if enter_button.button("Enter"):
        if image_choice:
            # Shows the image selected by the user
            col1, col2 = st.columns(2)
            with col1:
                display_image(image_choice, "Your Choice", width=150)
                
            img_array = preprocess_image(image_choice)

            # Predict the image class selected by the user
            prediction_result = classifier.predict(img_array)
            predicted_class_index = np.argmax(prediction_result)
            classes = ['paper', 'rock', 'scissors']
            classes_emoji = ['✋ Paper', '👊 Rock', '✌ Scissors']

            # Shows prediction results and probability
            st.write(f"<h2 style='font-size: 20px;'>Image Prediction Probabilities:</h2>", unsafe_allow_html=True)
            probabilities = prediction_result[0]
            for i, prob in enumerate(probabilities):
                st.text(f"{classes[i]}: {prob:.4f}")

            st.write(f"<h2 style='font-size: 20px;'>Image Prediction Result: {classes_emoji[predicted_class_index]}</h2>", unsafe_allow_html=True)
            my_choice_class_index = (predicted_class_index + 2) % 3

            # Show the 'my choice' image
            with col2:
                display_image(f"{classes[my_choice_class_index]}_1.png", "My Choice", width=150)

            # Updates the session state only when the "Enter" key is pressed
            st.session_state.state['image_choice'] = image_choice
            st.session_state.state['prediction_result'] = prediction_result

    if reset_button.button("Reset"):
        # Reset the session state
        st.session_state.state = {}
        st.experimental_rerun()

if __name__ == "__main__":
    main()
