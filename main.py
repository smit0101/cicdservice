import pymongo
import os

def main():
    # Connect to MongoDB
    client = pymongo.MongoClient(os.environ['MONGODB_URI'])
    database = client.get_default_database()

    # Example user data
    user_data = {
        'username': 'example_user',
        'email': 'user@example.com',
        'age': 25
    }

    # Insert user data into a 'users' collection
    database.users.insert_one(user_data)
    print('User data inserted successfully.')

if __name__ == "__main__":
    main()

