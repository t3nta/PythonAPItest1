from flask import Flask, request, jsonify

app = Flask(__name__)

#Får os til at spawne på home siden, som køres når man starter appen.
#@app.route("/")
#def home():
#    return "Home"

#GET route, skriv det her i http baren for at access det: http://127.0.0.1:5000/get-user/123?extra=%22hello%22
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "email@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

        return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

#Laver en if statement som kører appen efter validering
if __name__ == "__main__":
    app.run(debug=True)