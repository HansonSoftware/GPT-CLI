from curses import panel
import openai
from decouple import config

API_KEY = config("OPENAI_KEY")

openai.api_key = API_KEY

# Terminal Colors:
RED_TEXT = "\033[91m"
GREEN_TEXT = "\033[92m"
YELLOW_TEXT = "\033[93m"
BLUE_TEXT = "\033[94m"
RESET_TEXT = "\033[0m"

# models = openai.Model.list()
# print(models)

# response = openai.Completion.create(
#     model = "text-davinci-003",
#     prompt = "Hello",
#     temperature = 0.95,
#     max_tokens = 10,
# )

# print(response)

# textCompletion(model, prompt, temp)

# textEdit(model, prompt, temp)


# Command Line Interface:
def welcome():
    print("Welcome to the " + RED_TEXT + "DevX" + RESET_TEXT + " OpenAI Command Line Interface!")
    print("You will be prompted to enter some values to tweak the API call made to OpenAI")
    print(RED_TEXT + "Be sure to place your prompt into Prompt.txt!\n" + RESET_TEXT)
    print(GREEN_TEXT + "Use Case: " + RESET_TEXT + "[edit, complete] Enter one of these values.")
    print("    This controls which function called.\n    edit: ChatGPT will edit your prompt\n    complete: ChatGPT will respond to your prompt\n")
    print(BLUE_TEXT + "Model: " + RESET_TEXT + "[davinci, curie, babbage, ada] Enter one of these values.")
    print('    This controls which model to use, davinci is the "smartest".\n')
    print(YELLOW_TEXT + "Temperature: " + RESET_TEXT + "Enter a value between 0.0 and 1.0")
    print('    Temperature controls the "creativity" of the response.\n    1.0 is most "creative"')

def getInputs():
    useCase = input("Enter your desired " + GREEN_TEXT + "Use Case: " + RESET_TEXT)
    # TODO: Validate useCase, have user try again if invlid
    model = input("Enter the "+ BLUE_TEXT + "Model " + RESET_TEXT + "you want to use: ")
    # TODO: Validate model, have user try again if invlid
    temp = float(input("Enter a " + YELLOW_TEXT + "Temperture " + RESET_TEXT + "[0.0, 1.0]: "))
    # TODO: Validate float value, have user try again if invlid

    return useCase, model, temp

def printChoices(useCase, model, temp):
    print("\nYou Entered:")
    print("Use Case:", useCase)
    print("Model:", model)
    print("Temperature:", temp)

def main():
    welcome()
    useCase, model, temp = getInputs()
    file = open("prompt.txt", "r")
    prompt = file.read()
    printChoices(useCase, model, temp)
    print("Prompt:\n%s" % prompt)
    choice = input("\nProceed? (Y/n): ")
    if choice.lower() in ["y", "yes"]:
        print(GREEN_TEXT + "Proceeding..." + RESET_TEXT)
        # TODO: Correct function call will be made here.
    else:
        print(RED_TEXT + "Exiting..." + RESET_TEXT)

if __name__ == "__main__":
    main()
