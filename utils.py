from pprint import pprint
from wit import Wit
import random

access_token =  "XWXTNSYDG5B72A7276YSRVL7RQFWFO3J"
client = Wit(access_token = access_token)

def get_wit_response(message_text):
    wit_response = client.message(message_text)
    pprint(wit_response)
    entity = None
    #entity2 = None
    value = None
    #value2 = None
    intent = None
    try:
        entities = list(wit_response['entities'].keys())
        intent=wit_response['intents'][0]['name']
        for key in entities:
            entity = list(wit_response['entities'])[0]
            value = wit_response['entities'][key][0]['value']
        #for key in entities:
         #   entity2 = list(wit_response['entities'])[1]
          #  value2 = wit_response['entities'][key][0]['value']
           # break

    except:
        pass
    #return (intent,entity1,entity2,value2,value1)
    return(intent,entity,value)

    #value2 has the value of entity1
    #value1 has the value of entity2

def generate_user_response(messaging_text):
    intent,entity,value = get_wit_response(messaging_text)

    city={"foreign":["Spain","Turkey","Greece","Emirates"],"domestic":["Alexandria","Sharm el sheikh","Aswan","Luxor"]}

    bugdet={"2000":["Lotus Hotel","African House","The Australian Hostel"],"5000":["Novotel Hotel", "Sierra Hotel", "Arabella Azur Hotel"],"15000":["Steigenberger Hotel", "Jumeirah Beach Hotel", "Armani Hotel"]}

    response=None
    if intent=="send_greetings":
        response="Hello, how are you.\n1.Would you like to rate a city if so enter the city to be rated?\n2.Would you like a suggestion for a city if so enter your city?\n3.Would you like a suggestion for a residence if so enter number of travelers."

    elif intent == "rate_city" and entity == "city_to_rate:city_to_rate":
        response ="please enter you rate"
    elif intent == "rating_number" and entity == "rate:rate":
        response = "Done !"

    elif intent == "get_city" and entity == "current_city:current_city":
        response = "Would you like a domestic or Foregin Countries?"

    elif intent == "destinations_type" and entity == "travel_type:travel_type": 
        response = input("Would you like a Single city or Multiple cities?")
        if value in city.keys():
            if response == "single":
                x = random.randint(0, 4)
                response = city[value][x]
            else:
                response = city[value]

    elif intent == "get_travelers" and entity == "travelers_number:travelers_number":
        response = "Enter number of days you will spend"

    elif intent == "get_days" and entity == "days_number:days_number":
        response = "Enter your budget"

    elif intent == "get_budget" and entity == "budget_number:budget_number":
        if value in bugdet.keys():
            x = random.randint(0, 3)
            response = bugdet[value][x]
    else:
        response = "Sorry, i didn't understand you!"
    return response


#pprint(get_wit_response("hello"))
#pprint(get_wit_response("single"))
pprint(generate_user_response("5000"))
