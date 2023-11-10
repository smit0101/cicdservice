import pymongo
import os

def insert_user():
    # Connect to MongoDB
    client = pymongo.MongoClient(os.environ['MONGODB_URI'])
    database = client.get_default_database()

    # Example user data
    user_data = {
        'username': 'smitkalkani',
        'email': 'smitkalkani@smitsoft.com',
        'age': 24
    }

    # Insert user data into a 'users' collection
    database.users.insert_one(user_data)
    print('User data inserted successfully.')

def fetch_and_display_users():
    # Connect to MongoDB
    client = pymongo.MongoClient(os.environ['MONGODB_URI'])
    database = client.get_default_database()

    # Fetch all user data from the 'users' collection
    users = database.users.find()

    # Display user data
    print('User Data:')
    for user in users:
        print(f"Username: {user['username']}, Email: {user['email']}, Age: {user['age']}")

if __name__ == "__main__":
    insert_user()
    fetch_and_display_users()

