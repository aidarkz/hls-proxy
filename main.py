from flask import Flask, request, Response
import subprocess

app = Flask(__name__)

@app.route('/stream')
def stream():
    cmd = request.args.get('cmd')
    if not cmd:
        return "Missing 'cmd' parameter", 400

    ffmpeg_cmd = [
        'ffmpeg', '-i', cmd,
        '-f', 'mpegts',
        '-codec:v', 'mpeg1video',
        '-codec:a', 'mp2',
        '-'
    ]

    def generate():
        process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        try:
            while True:
                data = process.stdout.read(1024)
                if not data:
                    break
                yield data
        finally:
            process.kill()

    return Response(generate(), mimetype='video/mp2t')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
