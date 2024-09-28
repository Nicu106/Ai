
import requests
import urllib.parse  # Importing urllib to handle URL encoding


#this is __main__
def llm_set_txt_to_json(cv_promt):
    # Define the base URL and the variable content
    base_url = "https://hercai.onrender.com/turbo/hercai"
    # Updated parameters to ensure the response contains specific keys
    parameters = (
        'Please return a JSON object with the following keys: '
        '"nume", "varsta", "sex", "stare_viviala", "experienta_profesionala", '
        '"permis_de_conducere, "'
        '"educatie", "limbi_straine", "Abilitatit". If any value is not found in the CV, '
        'set it to null. value  '
    )
    # URL-encode the parameters and question
    encoded_parameters = urllib.parse.quote(parameters)
    encoded_question = urllib.parse.quote(cv_promt)

    # Send a GET request with the query parameter 'parameters' and 'question'
    response = requests.get(f"{base_url}?&question={str(cv_promt) + parameters}")

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        reply = data.get('reply')
        # Print the response content
        return reply
    else:
         return response.status_code