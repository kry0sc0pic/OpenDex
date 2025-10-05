from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_cors import CORS
from flask_restful import Api, Resource
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

# Load environment variables from a .env file
load_dotenv()

# --- Flask App Initialization ---

# The main Flask application instance.
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for the app to allow API requests
# from different origins.
CORS(app)

# The Flask-RESTful API extension instance, which simplifies the creation of APIs.
api = Api(app)


# --- Route Definitions ---

@app.route("/")
def index():
    """Renders the main page of the application.

    This function is responsible for rendering the `index.html` template,
    which serves as the main user interface for the OpenDex application.

    Returns:
        The rendered `index.html` template.
    """
    return render_template("index.html")


class OpenDexApi(Resource):
    """
    Provides the core API endpoint for the OpenDex application.

    This class inherits from `flask_restful.Resource` and handles all logic
    for the `/api` endpoint. It is responsible for receiving user prompts,

    interacting with the Langchain CSV agent, and returning the model's
    response.
    """

    def post(self):
        """
        Processes a POST request containing a user's prompt and returns a response.

        This method extracts a JSON payload from the request, which should
        contain the user's prompt, their OpenAI API key, and an optional model
        specification. It then initializes the appropriate OpenAI model, creates
        a Langchain CSV agent configured with the Pokémon dataset, and runs the
        agent to get an answer.

        The request body must be a JSON object with the following keys:
        - "prompt" (str): The user's question or prompt for the agent.
        - "key" (str): The user's OpenAI API key.
        - "model" (str, optional): The name of the OpenAI model to use
          (e.g., "gpt-3.5-turbo"). Defaults to "text-davinci-003".

        Returns:
            A tuple containing a JSON response and an HTTP status code.
            - On success (200 OK), it returns a JSON object with the original
              prompt and the agent's output.
            - On bad request (400), if "prompt" or "key" is missing, it
              returns a JSON error message.
            - On internal server error (500), it returns a JSON error
              message for any other exceptions.
        """
        jsonData = request.get_json(force=True)
        prompt = jsonData.get("prompt", None)
        api_key = jsonData.get("key", None)
        model = jsonData.get("model", "text-davinci-003")

        if not prompt:
            return {"error": "prompt is required"}, 400
        if not api_key:
            return {"error": "key is required"}, 400

        try:
            # Select the OpenAI model based on the request
            if model == "text-davinci-003":
                openai_model = OpenAI(
                    temperature=0.1,
                    model="text-davinci-003",
                    openai_api_key=api_key,
                )
            else:
                openai_model = ChatOpenAI(
                    temperature=0.1, model="gpt-3.5-turbo", openai_api_key=api_key
                )

            # Create and run the Langchain agent
            agent = create_csv_agent(
                openai_model, "datasets/pokedex_04_21.csv", verbose=True
            )
            op = agent.run(prompt)
            return {"prompt": prompt, "output": op}, 200
        except Exception as e:
            # Handle potential errors during API calls or agent execution
            return {"error": str(e)}, 500


# Register the OpenDexApi resource with the /api endpoint.
api.add_resource(OpenDexApi, "/api")

# --- Main Execution ---

if __name__ == "__main__":
    # Run the Flask app in debug mode for development.
    # This should be changed for a production environment.
    app.run(debug=True)