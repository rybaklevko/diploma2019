from flask import request, Response, render_template
from app import camera, app

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed', methods=['POST', 'GET'])
def video_feed():
    return Response(gen(camera.VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed_page', methods=['POST', 'GET'])
def video_feed_page():
    return render_template("live_streaming.html")