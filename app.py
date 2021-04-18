"""Flask app for Cupcakes"""

from flask import Flask, redirect, render_template
from models import Cupcake, db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sb_cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "aiofsf29347293sjfdv"

connect_db(app)
db.create_all()

def serialize_cupcake(cupcake):
    """Serialize cupcake SQLAlchemy object to dictionary."""

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image,
    }

@app.route('/api/cupcakes')
def get_cupcakes():
    """Fetch data about all cupcakes."""

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)
