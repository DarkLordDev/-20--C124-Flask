from flask import Flask, jsonify, request

app = Flask(__name__)


tasks = [
    {"id": 1, "title": "Demo Title", "description": "Demo desc", "done": False},
    {"id": 2, "title": "Demo Title 2", "description": "Demo desc 2", "done": False},
]


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/add-data", methods=["POST"])
def addData():
    if not request.json:
        return jsonify({"status": "error", "message": "Please provide data"}, 400)

    task = {
        "id": tasks[-1]["id"] + 1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False,
    }
    tasks.append(task)
    return jsonify({"status": "success", "message": "task added Successfully!!!"})


@app.route("/get-data", methods=["GET"])
def getData():
    return jsonify({"tasks": tasks})


if __name__ == "__main__":
    app.run(debug=False)
