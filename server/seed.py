#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import User, Artist, Museum, Review

if __name__ == "__main__":
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

    # Clear existing data
    # User.query.delete()
    # Artist.query.delete()
    # Museum.query.delete()
    # Review.query.delete()  # Clear existing reviews

    for _ in range(20):
        username = fake.profile(fields=["username"])["username"]
        user = User(username=username)

        # user.password_hash = (
        #     username  # We are calling the password_hash setter method here
        # )
        db.session.add(user)
        db.session.commit()

    artists = [
        "Vincent van Gogh",
        "Leonardo da Vinci",
        "Pablo Picasso",
        "Claude Monet",
        "Michelangelo",
    ]

    for artist_name in artists:
        artist = Artist(name=artist_name)
        db.session.add(artist)

    museum_and_cities = [
        {"name": "Louvre", "city": "Paris"},
        {"name": "Metropolitan Museum of Art", "city": "New York"},
        {"name": "National Gallery", "city": "London"},
        {"name": "Uffizi", "city": "Florence"},
        {"name": "Rijksmuseum", "city": "Amsterdam"},
        {"name": "Musee D'Orsay", "city": "Paris"},
    ]
    for item in museum_and_cities:
        museum = Museum(name=item["name"], city=item["city"])
        db.session.add(museum)


def add_reviews(num_reviews=50):
    for _ in range(num_reviews):
        user_id = fake.random_int(
            min=1, max=20
        )  # Replace with the actual range of user IDs
        artist_id = fake.random_int(
            min=1, max=5
        )  # Replace with the actual range of artist IDs
        museum_id = fake.random_int(
            min=1, max=6
        )  # Replace with the actual range of museum IDs
        text = fake.paragraph(nb_sentences=3)
        rating = fake.random_int(min=1, max=5)

        review = Review(
            user_id=user_id,
            artist_id=artist_id,
            museum_id=museum_id,
            text=text,
            rating=rating,
        )

        db.session.add(review)

    add_reviews()  # Add reviews to the database

    db.session.commit()


print("Database has been seeded.")
