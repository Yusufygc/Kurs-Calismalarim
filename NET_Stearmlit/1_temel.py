import streamlit as st

def cizgi():
    st.text("*********************************************************************************************************")

cizgi()
st.title("Hello GeeksForGeeks !!!")
st.header("This is a header") 
st.subheader("This is a subheader")

cizgi()

st.text("Hello GeeksForGeeks!!!")

cizgi()

# 4. Markdown
# This example uses st.markdown() to show formatted text. 
# The ### creates a level 3 header, used for medium-sized headings in the app.

st.markdown("### This is a markdown")
cizgi()

st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
cizgi()

# Write
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))

cizgi()

from PIL import Image  # Import Image from Pillow
img = Image.open("img1.jpg") # Open the image file
st.image(img, width=200) # Display the image with a specified width

cizgi()

# 8. Checkbox
# This example uses a checkbox in Streamlit to toggle content visibility. 
# When the checkbox labeled "Show/Hide" is checked, 
# it displays a text message on the screen.
# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    # Show this text only when the checkbox is checked
    st.text("Showing the widget")

cizgi()

# 9. Radio Button

# This example demonstrates how to use 
# radio buttons to let users select one option from a list. 
# Based on the selected gender, 
# the app displays the result using st.success()

# Create a radio button to select gender
status = st.radio("Select Gender:", ['Male', 'Female'])

# Display the selected option using success message
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

cizgi()
# 10. Selection Box

# This example uses a select box in Streamlit 
# to let users choose one option from a dropdown list. 
# The selected item is then displayed on the screen.
# Create a dropdown menu for selecting a hobby
hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])

# Display the selected hobby
st.write("Your hobby is:", hobby)

cizgi()

# 11. Multi-Selectbox

# This example demonstrates how to use a multiselect box in Streamlit, 
# allowing users to choose multiple options from a list.
# The app then displays the number of selected items.
# Create a multiselect box for choosing hobbies
hobbies = st.multiselect("Select Your Hobbies:", ['Dancing', 'Reading', 'Sports'])

# Display the number of selected hobbies
st.write("You selected", len(hobbies), "hobbies")

cizgi()

# 12. Button

# This example shows how to use buttons in Streamlit.
# Buttons can trigger specific actions when clicked,
# such as displaying a message or running a function.

# A simple button that does nothing
st.button("Click Me")

# A button that displays text when clicked
if st.button("About"):
    st.text("Welcome to GeeksForGeeks!")

cizgi()

# 13. Text Input

# Text input fields allow users to enter custom data. 
# This example collects a user's name, 
# formats it with proper capitalization and 
# displays it when Submit button is clicked, 
# simulating a basic form interaction.

# Create a text input box with a default placeholder
name = st.text_input("Enter your name", "Type here...")

# Display the name after clicking the Submit button
if st.button("Submit"):
    result = name.title()  # Capitalize the first letter of each word
    st.success(result)

cizgi()

# 14.  Slider

# Sliders provide a way to select numeric values within a range. 
# This example lets users choose a level between 1 and 5 and 
# displays the selected value instantly. 
# It is useful for settings like ratings, 
# difficulty levels or thresholds.

# Create a slider to select a level between 1 and 5
level = st.slider("Choose a level", min_value=1, max_value=5)

# Display the selected level
st.write(f"Selected level: {level}")

cizgi()