from flask import Flask, render_template, request,jsonify
from openai import OpenAI

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('chat.html')
  
@app.route('/get', methods=['GET','POST'])
def chat():
  msg=request.form['msg']
  input=msg
  return get_Chat_response(input)

client = OpenAI(api_key='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')
messages = [{"role": "system", "content": "You have general knowledge of everything"}]

def get_Chat_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply
  
if __name__ =='__main__':
  app.run()  