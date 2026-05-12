from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return {
        'status': 'Online ✅',
        'message': 'Вітаємо на твоєму Azure Web App!',
        'runtime': 'Python 3.14'
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
