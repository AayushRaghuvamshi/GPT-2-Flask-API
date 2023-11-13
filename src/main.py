from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")


@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    inputs = tokenizer.encode(data['text'], return_tensors='pt')
    outputs = model.generate(
        inputs,
        max_length=1000,
        num_return_sequences=1,
        temperature=0.5,
        top_k=40,ss
        top_p=0.9,
        no_repeat_ngram_size=2
    )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify(text=text)


if __name__ == '__main__':
    app.run(debug=True)
