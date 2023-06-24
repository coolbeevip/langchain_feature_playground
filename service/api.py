# -*- coding: UTF-8 -*-

import json

from flask import Flask, request, jsonify

from service.langchain_openai import LangChainOpenAI
from service.langchain_type import ChainType

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

openai_conversations = {}


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route('/api/upload', methods=['POST'])
def upload_file():
    # 检查是否有文件上传
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # 检查文件是否有文件名
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 如果文件存在，保存文件
    if file:
        file.save(file.filename)

        return jsonify({'message': 'File uploaded successfully'}), 200


@app.route('/api/openai/agent', methods=['POST'])
def openai_agent():
    request_json = request.get_json()
    langchain_openai = LangChainOpenAI().get_langchain_openai(ChainType.AGENT)
    answer = langchain_openai.get_answer(request_json['question'])
    json_data = json.dumps({'answer': answer}, ensure_ascii=False)
    return app.response_class(json_data, 200, mimetype='application/json')


@app.route('/api/openai/conversation/<session_id>', methods=['POST'])
def openai_conversations(session_id):
    request_json = request.get_json()
    if session_id in openai_conversations:
        langchain_openai = openai_conversations[session_id]
    else:
        langchain_openai = LangChainOpenAI().get_langchain_openai(ChainType.CONVERSATION)
        openai_conversations[session_id] = langchain_openai

    answer = langchain_openai.get_answer(request_json['question'])
    json_data = json.dumps({'answer': answer}, ensure_ascii=False)
    return app.response_class(json_data, 200, mimetype='application/json')


@app.route('/api/openai/documents', methods=['POST'])
def openai_documents():
    request_json = request.get_json()
    langchain_openai = LangChainOpenAI().get_langchain_openai(ChainType.DOCUMENT)
    answer = langchain_openai.get_answer(request_json['question'])
    json_data = json.dumps({'answer': answer}, ensure_ascii=False)
    return app.response_class(json_data, 200, mimetype='application/json')
