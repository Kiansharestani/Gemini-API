import google.generativeai as genai

API_KEY = "AIzaSyAZHy37GX8WZJLRdz1GEpERNfKBDZMfT2g" 
Exits_Massages = {"Exit", "Quit", "exit", "quit", "Khrooj", "Tamam", "خروج"}

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")
chat = model.start_chat(history=[])

print("Hello I'am Kian AI.")

while True:
    user_message = input("Your Massage :   ")
    if user_message.lower() in Exits_Massages : 
        Exit = input("Exit? Press ENTER")
        break
    
    try:
        response = chat.send_message(user_message)
        print(f"Kian AI :{response.text}")
    except Exception as e:
        print(f"Error : {e}")
        print("Error : Please Try Agein !")
        Exit = input("Exit? Press ENTER")