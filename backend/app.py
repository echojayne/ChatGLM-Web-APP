from flask import Flask, request, jsonify, send_from_directory, render_template
# from flask_cors import CORS
import model

# 创建Flask应用
app = Flask(__name__, static_folder='../frontend/public', static_url_path='/') # 指定前端静态文件夹路径

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # 处理POST请求
        input_text = request.json.get('text', '')
        # print("==> input_text: ", input_text)
        response = model.chat(input_text)
        # print("==> response: ", response)
        return jsonify({'response': response})
    else:
        # 处理GET请求（可选，仅用于测试）
        return 'GET method is not recommended for this route.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8899)

