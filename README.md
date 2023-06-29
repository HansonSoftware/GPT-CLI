# DevX GPT-CLI
This is a Command Line Interface that can be used to interact with OpenAI's API.

### Getting Started
1. Clone this repo onto your machine
2. Place your prompt into Prompt.txt
3. If you plan to use "edit", place your text to modify in Input.txt
4. Start the CLI
```
cd GPT-CLI
python UseAPI.py
```
5. Follow the prompts and get a response from Chat-GPT!

### Parameters
Use Case:

Enter one of the following values: "edit" or "complete".
This determines which function will be called.
If you choose "edit", ChatGPT will edit your prompt.
If you choose "complete", ChatGPT will respond to your prompt.

Model:

Enter one of the following values: "davinci", "curie", "babbage", or "ada".
This determines which model to use.
"davinci" is considered the "smartest" model.
If your use case is "edit", the model will be preset for you.

Temperature:

Enter a value between 0.0 and 1.0.
Temperature controls the "creativity" of the response generated by ChatGPT.
A temperature of 1.0 results in the most "creative" responses.

### Supported Endpoints
/v1/completions
/v1/edits

### Coming Soon
Support for:

/v1/chat/completions with gpt-4 and gpt-3.5-turbo
