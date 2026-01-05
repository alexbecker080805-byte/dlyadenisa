from flask import Flask, render_template_string, send_file

app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Screamer Button</title>
        <style>
            body { margin: 0; height: 100vh; display: flex; justify-content: center; align-items: center; background: black; color: white; }
            button { width: 100%; height: 100%; font-size: 50px; background: red; color: white; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <button onclick="playSound()">PRESS ME</button>
        <audio id="sound" src="/static/skrimer-golden-freddi-fnaf-1.mp3" preload="auto"></audio>
        <script>
            function playSound() {
                var audio = document.getElementById('sound');
                audio.volume = 5.0;  // Установите громкость (может быть ограничено браузером)
                audio.play();
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_file('static/' + filename, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)