"""Flask app for Cupcakes"""

from forms import CupcakeForm
from flask import Flask, request, jsonify, render_template
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

@app.route('/')
def homepage():
    """Homepage route."""

    form = CupcakeForm()
    return render_template('main.html', form=form)

@app.route('/api/cupcakes', methods=['GET'])
def get_cupcakes():
    """Fetch data about all cupcakes."""

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake_details(cupcake_id):
    """Fetch data about one cupcake using cupcake ID."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialzed = serialize_cupcake(cupcake)

    return jsonify(cupcake=serialzed)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """Create cupcake from request data, and return JSON."""

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']

    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image or None)

    db.session.add(cupcake)
    db.session.commit()
    
    serialized = serialize_cupcake(cupcake)

    return (jsonify(cupcake=serialized), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """Update cupcake with data from request, and return JSON."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json['flavor']
    cupcake.size = request.json['size']
    cupcake.rating = request.json['rating']
    cupcake.image = request.json['image']

    db.session.add(cupcake)
    db.session.commit()

    serialzed = serialize_cupcake(cupcake)

    return jsonify(cupcake=serialzed)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Delete cupcake from DB."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='Deleted.')