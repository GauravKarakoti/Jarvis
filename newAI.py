import google.generativeai as genai
import os

def edd(user_input):
    os.environ["API_KEY"] = "AIzaSyDDAo7eJg2ubxXOEJAA8bnWEucYcjJjH3M" 
    genai.configure(api_key=os.environ["API_KEY"])

    model = genai.GenerativeModel("gemini-1.5-flash-latest")

    def get_gemini_response(prompt):
        response = model.generate_content(prompt)
        return response.text

    if user_input.lower() == "exit":
        return "Terminating... Goodbye!"
    
    response = get_gemini_response(user_input)

    cleaned_response = response.replace('*', '')

    words = cleaned_response.split()
    limited_response = " ".join(words[:50])

    return limited_response
