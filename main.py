from flask import Flask, request, jsonify

app = Flask(__name__)

#Får os til at spawne på home siden, som køres når man starter appen.
#@app.route("/")
#def home():
#    return "Home"

#GET route
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

#Laver en if statement som kører appen efter validering
if __name__ == "__main__":
    app.run(debug=True)