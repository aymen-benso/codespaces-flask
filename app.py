from flask import Flask, request, jsonify , render_template
import requests
from openai import OpenAI
import json
from testt import get_answer

google_api_key = "AIzaSyAZvPEKmK2qPK6TVaP9-tqOi3GpTAFanFU"
google_cx = "e3a2db6e7281d4629"


client = OpenAI(
    api_key='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',
    organization='org-yui7Ie8osHV9jytpHdWaIdRv',
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/api/get_ai_snippets', methods=['GET'])
def get_ai_snippets():
    query = request.args.get('query')
    gptv = request.args.get('gptv')
    try:
        completion = client.chat.completions.create(
        model=gptv,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}
        ]
        )

        return (json.dumps(completion.choices[0].message.content)) # if ChatCompletionMessage has a to_dict method
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/withsearch', methods=['GET'])
def test():

    results = get_answer(request.args.get('query'), request.args.get('gptv'))

    return json.dumps(results)

if __name__ == '__main__':
    app.run(debug=True)