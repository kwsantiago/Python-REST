from flask import Flask, json

names = [{"id": 1, "name": "Kyle Santiago"}, {"id": 2, "name": "Sandy Sue"}]

api = Flask(__name__)

@api.route('/names', methods=['GET'])
def get_names():
  return json.dumps(names)

@api.route('/names', methods=['POST'])
def post_names():
    return json.dumps({"success": True}), 201

if __name__ == '__main__':
    api.run()
