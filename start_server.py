from databases.database_manager import Database
import blueprints
from flask import Flask

# from blueprints.tool import tool_blueprint

# Loading config:
web_config = Database.read("config")

app = Flask(__name__)
app.config["SECRET_KEY"] = web_config["SECRET_KEY"]
if app.config["SECRET_KEY"] == "SECRET KEY HERE":
    print("DO NOT FORGET TO CHANGE SECRET KEY!!")
app.register_blueprint(blueprints.root_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Don't forget about 0.0.0.0 if you actually want things to connect
