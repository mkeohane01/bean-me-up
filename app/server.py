from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/conversation', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    print(question)

    # Use LLM pipeline here to generate the response
    
   
    return jsonify({'answer': f"This is the answer to {question}"})

if __name__ == '__main__':
    app.run(debug=True)