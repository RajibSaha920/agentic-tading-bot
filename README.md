### keys needs to be mention inside the .env
```
POLYGON_API_KEY
GOOGLE_API_KEY
TAVILY_API_KEY
GROQ_API_KEY
PINECONE_API_KEY
```

### for running the fastapi endpoint
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

```

### for running the streamlit ui
```
streamlit run streamlit_ui.py

```

### for installing the requirements
```
pip install -r requirements.txt
```

### for creating the env
```
python -m venv venv
```

### for activate the env through cmd
```
venv\Scripts\activate
```

### for activate the env through git-bash
```
source activate ./env
```

## Next step
1. mention logger and exception
2. capture the logging and exception messages
3. if possible run the langgraph workflow in ipynb and test the real time data fetching tool
4. deploy it
5. sit on it either thu or friday


models/deep-research-pro-preview-12-2025
models/gemini-embedding-001
models/gemini-embedding-2-preview
models/gemini-embedding-2
models/aqa
models/imagen-4.0-generate-001
models/imagen-4.0-ultra-generate-001
models/imagen-4.0-fast-generate-001
models/veo-3.1-generate-preview
models/veo-3.1-fast-generate-preview
models/veo-3.1-lite-generate-preview
models/gemini-2.5-flash-native-audio-latest
models/gemini-2.5-flash-native-audio-preview-09-2025
models/gemini-2.5-flash-native-audio-preview-12-2025
models/gemini-3.1-flash-live-preview
models/gemini-3.5-live-translate-preview

https://app.pinecone.io/organizations/-Ox0EqiY1ViG4TGjtQyr/projects/f3201d05-f9e8-4bc3-9cec-759731990018/indexes
https://console.groq.com/keys

https://app.tavily.com/home?utm_source=chatgpt.com

https://aistudio.google.com/api-keys?project=euphoric-hull-279915   

https://polygon.readthedocs.io/en/latest/Getting-Started.html?utm_source=chatgpt.com

https://massive.com/dashboard/keys