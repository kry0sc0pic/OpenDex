from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_cors import CORS
from flask_restful import Api, Resource
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route("/")
def index():
    return render_template("index.html")


class OpenDexApi(Resource):
    def post(self):
        jsonData = request.get_json(force=True)
        prompt = jsonData.get("prompt", None)
        api_key = jsonData.get("key", None)
        model = jsonData.get("model", "text-davinci-003")
        if prompt == None:
            return {"error": "prompt is required"}, 400
        if api_key == None:
            return {"error": "key is required"}, 400

        else:
            try:
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
                agent = create_csv_agent(
                    openai_model, "datasets/pokedex_04_21.csv", verbose=True
                )
                op = agent.run(prompt)
                return {"prompt": prompt, "output": op}, 200
            except Exception as e:
                return {"error": str(e)}, 500


api.add_resource(OpenDexApi, "/api")

if __name__ == "__main__":
    app.run(debug=True)
