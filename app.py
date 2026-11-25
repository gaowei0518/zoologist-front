import streamlit as st
import requests
"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)

"""
## Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin. We need to know all the inputs required by our model to make a prediction.

1. Let's ask for:
- island (the location where the penguin lives: Biscoe, Dream or Torgersen)
- bill length (in mm)
- bill depth (in mm)
- flipper length (in mm)
- body mass (in g)
- sex ("Male" or "Female")
"""

island = st.text_input('island (the location where the penguin lives: Biscoe, Dream or Torgersen)', 'Torgersen')
bill_len = st.number_input('bill length  (in mm)', 0)
bill_dep = st.number_input('bill depth  (in mm)', 0)
flipper_len = st.number_input('flipper length  (in mm)', 0)
body_mass = st.number_input('body mass (in g)', 0)
sex = st.text_input('sex ("Male" or "Female")', 'Male')


"""
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?

1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""
#predict?island=Dream&bill_length_mm=51.9&bill_depth_mm=19.5&flipper_length_mm=206.0&body_mass_g=3950.0&sex=Male
param = {"island":island,
         "bill_length_mm":float(bill_len),
         "bill_depth_mm":float(bill_dep),
         "flipper_length_mm":float(flipper_len),
         "body_mass_g":float(body_mass),
         "sex":sex
    }

base_url = st.secrets['BASE_URL']

if st.button('click me to predict'):
    res = requests.get(base_url,params=param)

    if res.status_code == 200:
        data = res.json()  # Extract the JSON content
        st.write("Prediction results:")
        st.json(data)  # Formats JSON cleanly in Streamlit
    else:
        st.error(f"Error {res.status_code}: {res.text}")
