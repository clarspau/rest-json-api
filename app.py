"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)

# Configuration for SQLAlchemy and Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret-sweets"

# Connect to the database
connect_db(app)


@app.route("/")
def home():
    """Homepage."""

    return render_template("index.html")


@app.route("/api/cupcakes")
def list_cupcakes():
    """Return a list of all cupcakes.

    Returns JSON like:
        {cupcakes: [{id, flavor, rating, size, image}, ...]}
    """

    # Query all cupcakes from the database
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Add cupcake, and return data about the new cupcake.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    data = request.json

    # Create a new cupcake object from the request data
    cupcake = Cupcake(
        flavor=data['flavor'],
        size=data['size'],
        rating=data['rating'],
        image=data['image'] or None
    )

    # Add and commit the new cupcake to the database
    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.to_dict()), 201)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Return data on a specific cupcake.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    # Query the specific cupcake by its ID
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update a cupcake from data in the request. Return updated data.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    data = request.json

    # Query the specific cupcake by its ID
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    # Update the cupcake attributes with the new data
    cupcake.flavor = data["flavor"]
    cupcake.size = data["size"]
    cupcake.rating = data["rating"]
    cupcake.image = data["image"]

    # Commit the changes to the database
    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def remove_cupcake(cupcake_id):
    """Delete a cupcake and return a confirmation message.

    Returns JSON like:
        {message: "Deleted"}
    """

    # Query the specific cupcake by its ID
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    # Delete the cupcake and commit the changes
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")


def run_app():
    app.run(debug=True)


if __name__ == '__main__':
    run_app()
