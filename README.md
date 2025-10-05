# OpenDex: Your Pokémon AI Assistant

OpenDex is a web application that acts as a "ChatGPT for Pokémon." It uses the power of OpenAI's language models and Langchain to answer your questions about Pokémon, based on a comprehensive dataset. You can ask it anything from "Who is the strongest Pokémon?" to "What are the weaknesses of Charizard?"

## Purpose

This project serves as a demonstration of how to build a simple, data-driven chatbot using modern AI tools. It integrates a Flask backend with Langchain's CSV agent to create an interactive experience where users can query a structured dataset (a Pokedex CSV file) in natural language.

## Project Structure

```
.
├── datasets/
│   └── pokedex_04_21.csv   # The core Pokémon dataset
├── static/
│   ├── index.js            # Frontend JavaScript logic
│   └── styles.css          # Styles for the frontend
├── templates/
│   └── index.html          # The main HTML page for the UI
├── .env.example            # Example environment file
├── app.py                  # The main Flask application logic
├── LICENSE                 # Project license
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

## Setup Instructions

Follow these steps to get the OpenDex application running on your local machine.

### 1. Clone the Repository

First, clone this repository to your local machine:
```bash
git clone https://github.com/example/opendex.git
cd opendex
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Install all the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Set Up Your OpenAI API Key

The application requires an OpenAI API key to function.

1.  **Get a key:** If you don't have one, create an API key on the [OpenAI platform](https://platform.openai.com/account/api-keys).
2.  **Create a `.env` file:** Rename the `.env.example` file to `.env`.
3.  **Add your key:** Open the `.env` file and paste your API key into it, like so:

    ```
    OPENAI_API_KEY="sk-YourSecretKeyHere..."
    ```

### 5. Run the Application

With everything set up, you can now run the Flask web server:
```bash
python app.py
```
The application will be accessible at `http://127.0.0.1:5000` in your web browser.

## Usage

There are two ways to interact with OpenDex:

### 1. Web Interface

Navigate to `http://127.0.0.1:5000` in your browser. You will see a simple interface where you can enter your OpenAI API key and a prompt. The application will then display the Pokémon-related answer.

### 2. API Endpoint

You can also interact with the application programmatically by sending a POST request to the `/api` endpoint.

Here is an example using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/api \
     -H "Content-Type: application/json" \
     -d '{
           "key": "YOUR_OPENAI_API_KEY",
           "prompt": "How many legs does a Metapod have?",
           "model": "gpt-3.5-turbo"
         }'
```

**Request Body:**

*   `key` (string, required): Your OpenAI API key.
*   `prompt` (string, required): The question you want to ask about Pokémon.
*   `model` (string, optional): The OpenAI model to use (e.g., `text-davinci-003`, `gpt-3.5-turbo`). Defaults to `text-davinci-003`.

**Success Response (200 OK):**

```json
{
  "output": "Metapod does not have any legs.",
  "prompt": "How many legs does a Metapod have?"
}
```

## Dataset

This project uses the [**Complete Pokemon Dataset**](https://www.kaggle.com/datasets/mariotormo/complete-pokemon-dataset-updated-090420?select=pokedex_%28Update_04.21%29.csv) provided by Mario Tormo Romero on Kaggle.

## Watch the Video

See a walkthrough of the project on YouTube:
[https://youtu.be/hpps9CKD0pk](https://youtu.be/hpps9CKD0pk)

## License

This project is licensed under the **GNU AGPL v3**. See the `LICENSE` file for more details.