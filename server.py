from flask import Flask, jsonify, request, abort

from download import downloadImage, deleteImage
from tag import getTag

app = Flask(__name__)


@app.route('/get-tags', methods=['GET'])
def index():
    url = request.args.get("url")
    loc = downloadImage(url)
    if loc is None:
        abort(400)
    res = getTag(loc)
    deleteImage(loc)
    return jsonify(res)

@app.errorhandler(400)
def error():
    return jsonify({"Error": "Could not download image, please send the correct url or try again later."})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="8081")
