# OpenDex
### ChatGPT for Pokemon. Powered by [OpenAI GPT-3](https://openai.com/) and [Langchain](https://github.com/hwchase17/langchain)


## Dataset
[**Complete Pokemon Dataset** by *Mario Tormo Romero*](https://www.kaggle.com/datasets/mariotormo/complete-pokemon-dataset-updated-090420?select=pokedex_%28Update_04.21%29.csv)


## Setup
### 1) Create OpenAI API Key [here](https://platform.openai.com/account/api-keys)
### 2) Paste Key in `.env.example` so it looks like this
```bash
OPENAI_APK_KEY="sk-...aup2"
```

### 3) Rename `.env.example` to `.env`

### 4) Create Virtual Environment in the root folder and activate
```bash
virtualenv venv
venv\Scripts\activate # -> windows
source venv/bin/activate # -> linux/mac
```

### 5) Install Dependencies
```bash
pip install -r requirements.txt
```

### 6) Run Flask Web Server
```bash
python app.py
```



### 

## License
### GNU AGPL v3


## Youtube Video
https://youtu.be/hpps9CKD0pk