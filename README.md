# chat-gpt-rpg

Welcome to `Chat-GPT-RPG`, a fun and quirky project aimed at learning to code. 

The goal of the project are as follows: 
- Provide an opportunity for learning to code while exploring the fascinating realm of AI using Chat GPT.
- Play around with [Chat-GPT API](https://platform.openai.com/docs/introduction/overview) provided by OpenAI using Python `openai` module.
- Explore the possibilities and see how AI can transform various tasks and applications.
- Interact with our AI-powered chatbot, an intelligent virtual assistant that can provide information, answer questions, and even engage in entertaining conversations. 
- Discover the capabilities of conversational AI firsthand.


## Get started
To run the project locally please follow the below steps:

1. Install Poetry please check the official Poetry documentation for the instructions:

    https://pypi.org/project/poetry/ \
    https://python-poetry.org/docs

2. Go the the project's main directory and install all the required dependencies by running the following command in the Terminal:
``` console
poetry install
```
Start the Poetry shell:
``` console
poetry shell
```

3. The OpenAI API uses API keys for authentication. In addition to the API key you need to specify which organization is used for an API request.

Please visit your [API Keys page](https://platform.openai.com/account/api-keys) to retrieve the API key you'll use in your requests and [Organization settings page](https://platform.openai.com/account/org-settings) to set up your Organization ID. 

The program will read your API Key and Organization ID from `.secrets.toml` file from `src/config` directory, so please make sure you created it, as follows:

filepath: `src/config/secrets.toml`
file content:
``` toml
OPENAI_API_KEY="REPLACE_WITH_YOUR_OPENAI_API_KEY"
organization = "REPLACE_WITH_YOUR_ORGANIZATION_ID"
```

4. Run the Flask project by running the following command in the Terminal:
``` console
flask --app src/app run
```


**Have fun!**

## Disclaimer

Chat-GPT-RPG is an ongoing project that's constantly evolving. Remember, the content here is for educational purposes only.

More documentation on existing endpoints will follow.