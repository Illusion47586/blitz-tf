from flask import Flask, jsonify, request, abort

from download import downloadImage, deleteImage
from tag import getTag

app = Flask(__name__)


@app.route('/get-tags', methods=['GET'])
def index():
    url = request.args.get("url")
    try:
        loc = downloadImage(url)
        if loc is None:
            abort(400)
        res = getTag(loc)
        if res is None:
            abort(400)
        deleteImage(loc)
        response = jsonify(res)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except:
        abort(400)


@app.errorhandler(400)
def error():
    return jsonify({"Error": "Could not download image, please send the correct url or try again later."})
