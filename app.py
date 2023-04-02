from flask import Flask, render_template, request
from flask_restful import Api, Resource
from flask_cors import CORS
from langchain.llms import OpenAI
from langchain.agents import create_csv_agent
from dotenv import load_dotenv
load_dotenv()
agent = create_csv_agent(OpenAI(temperature=0.1),
                         'datasets/pokedex_04_21.csv', verbose=True)
app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')


class OpenDexApi(Resource):
    def post(self):
        jsonData = request.get_json(force=True)
        prompt = jsonData['prompt']
        if (prompt == None):
            return {'error': 'prompt is required'}, 400
        else:
            try:
                op = agent.run(prompt)
                return {'prompt': prompt, 'output': op}, 200
            except Exception as e:
                return {'error': str(e)}, 500


api.add_resource(OpenDexApi, '/api')

if __name__ == '__main__':
    app.run(debug=True)
