from flask import Flask, render_template
import base64

CONFIG = {
    'stu_name': '黄致远',
    'stu_id': '2020140180',
    'department': '人工智能学院',
    'status': '允许入校',
    'image_path': 'demo_img.jpeg'
}

app = Flask(__name__)
with open(CONFIG['image_path'], 'rb') as f:
    base64_img = base64.b64encode(f.read()).decode()


@app.route('/')
def hello():
    return render_template('index.html',
                           base64_img=base64_img,
                           stu_name=CONFIG['stu_name'],
                           stu_id=CONFIG['stu_id'],
                           department=CONFIG['department'],
                           status=CONFIG['status'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, )
