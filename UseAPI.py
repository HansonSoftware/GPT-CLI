import openai
from decouple import config
import json

API_KEY = config("OPENAI_KEY")

openai.api_key = API_KEY

# Terminal Colors:
RED_TEXT = "\033[91m"
GREEN_TEXT = "\033[92m"
YELLOW_TEXT = "\033[93m"
BLUE_TEXT = "\033[94m"
RESET_TEXT = "\033[0m"

# Prints all available Models
# models = openai.Model.list()
# print(models)

def chatCompletion(model, system, prompt, temp):
    response = openai.ChatCompletion.create(
        model = model,
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        # feel free to adjust max_tokens to your needs
        max_tokens = 10,
        temperature = temp
    )
    return response;


def textCompletion(model, prompt, temp):
    response = openai.Completion.create(
        model = model,
        prompt = prompt,
        temperature = temp,
        #feel free to adjust max_tokens to your needs
        max_tokens = 10
    )
    return response

def textEdit(model, prompt, inputValue, temp):
    response = openai.Edit.create(
        model = model,
        instruction = prompt,
        temperature = temp,
        input = inputValue,
        top_p = 1
    )
    return response


# Command Line Interface:
def welcome():
    print("Welcome to the " + RED_TEXT + "DevX" + RESET_TEXT + " OpenAI Command Line Interface!")
    print("You will be prompted to enter some values to tweak the API call made to OpenAI")
    print(RED_TEXT + "Be sure to place your prompt into Prompt.txt!" + RESET_TEXT)
    print(RED_TEXT + "If you plan to edit, be sure to place your text to modify into Input.txt!" + RESET_TEXT)
    print(RED_TEXT + "If you plan to chat, be sure to place your system prompt into System.txt!" + RESET_TEXT)
    print(GREEN_TEXT + "Use Case: " + RESET_TEXT + "[edit, complete, chat] Enter one of these values.")
    print("    This controls which function called.\n    edit: ChatGPT will edit your prompt\n    complete: ChatGPT will respond to your prompt\n    chat: Chat with the gpt-4 or gpt-3.5 models!\n")
    print(BLUE_TEXT + "Model: " + RESET_TEXT + "complete: [davinci, curie, babbage, ada], chat: [gpt-4, gpt-3.5-turbo] Enter one of these values.")
    print('    This controls which model to use, davinci is the "smartest".\n    If your use case is "edit", the model will be preset.')
    print(YELLOW_TEXT + "Temperature: " + RESET_TEXT + "Enter a value between 0.0 and 1.0")
    print('    Temperature controls the "creativity" of the response.\n    1.0 is most "creative"\n')

def getInputs():
    # Use Case Validation:
    while True:
        useCase = input("Enter your desired " + GREEN_TEXT + "Use Case: " + RESET_TEXT)
        if useCase.lower() == "edit" or useCase.lower() == "complete" or useCase.lower() == "chat":
            break
        else:
            print("Invalid use case. Please enter either 'edit' or 'complete'. Try again.")
    if useCase.lower() == "chat":
        #TODO: Model validation for 
        validModels = ["gpt-4", "gpt-3.5-turbo"]
        model = input("Enter the "+ BLUE_TEXT + "Model " + RESET_TEXT + "you want to use: ")
    if useCase.lower() == "code" or useCase.lower() == "edit": 
        # Model Validation:
        validModels = ["davinci", "curie", "babbage", "ada"]
        while True:
            if(useCase.lower() == "complete"):
                model = input("Enter the "+ BLUE_TEXT + "Model " + RESET_TEXT + "you want to use: ")
                if model.lower() in validModels:
                    if(model == "davinci"):
                        model = "text-davinci-003"
                    elif(model == "curie"):
                        model = "text-curie-001"
                    elif(model == "babbage"):
                        model = "text-babbage-001"
                    elif(model == "ada"):
                        model = "text-ada-001"
                    break
                else:
                    print("Invalid model. Please enter either 'davinci', 'curie', 'babbage', or 'ada'. Try again.")
            else: 
                model = "text-davinci-edit-001"
                break
    # Temperature Validation:
    while True:
        try:
            temp = float(input("Enter a " + YELLOW_TEXT + "Temperature " + RESET_TEXT + "[0.0, 1.0]: "))
            if (0.0 <= temp <= 1.0):
                break
            else:
                print("Invalid temperature. Please enter a float value between [0.0 and 1.0]. Try again.")
        except ValueError:
            print("Invalid temperature. Please enter a valid float value. Try again.")

    return useCase, model, temp

def printChoices(useCase, model, temp):
    print("\nYou Entered:")
    print(GREEN_TEXT + "Use Case:" + RESET_TEXT, useCase)
    print(BLUE_TEXT + "Model:" + RESET_TEXT, model)
    print(YELLOW_TEXT + "Temperature:" + RESET_TEXT, temp)

def main():
    welcome()
    useCase, model, temp = getInputs()
    file = open("Prompt.txt", "r")
    prompt = file.read()
    file.close()
    printChoices(useCase, model, temp)
    print("Prompt:\n%s" % prompt)

    if(useCase.lower() == "edit" or useCase.lower() == "chat"):
        file = open("Input.txt" , "r")
        inputValue = file.read()
        file.close()
        print("Input:\n%s" % inputValue)
    
    choice = input("\nProceed? (Y/n): ")

    if choice.lower() in ["y", "yes"]:
        print(GREEN_TEXT + "Proceeding..." + RESET_TEXT)
        print("\nChat GPT Output:")
        if (useCase.lower() == "chat"):
            response = json.loads(str(chatCompletion(model, inputValue, prompt, temp)))
            print(response['choices'][0]['message']['content'])
        if(useCase.lower() == "complete"):
            response = json.loads(str(textCompletion(model, prompt, temp)))
            print(response['choices'][0]['text'])
        elif(useCase.lower() == "edit"):
            response = json.loads(str(textEdit(model, prompt, inputValue, temp)))
            print(response['choices'][0]['text'])
    else:
        print(RED_TEXT + "Exiting..." + RESET_TEXT)

if __name__ == "__main__":
    main()
