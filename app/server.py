from flask import Flask, render_template, request, jsonify, session
from app.prompting import build_assistant, build_thread, process_user_message

app = Flask(__name__)
app.secret_key = 'secret_session_key'


@app.route('/')
def index():
    session['assistant_ID'] = build_assistant()
    thread_ID, message = build_thread()
    session['thread_ID'] = thread_ID
    return render_template('index.html', start_message=message.strip())

@app.route('/api/conversation', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    # Use LLM pipeline here to generate the response
    response = process_user_message(question, session['thread_ID'], session['assistant_ID'])
    # print(response)
    # print(session)
    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True)