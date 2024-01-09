from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from flask_cors import CORS
import requests
import json
import pandas as pd
from sklearn.preprocessing import normalize
from pymongo import MongoClient
app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb+srv://jjpark57:baseball101@cluster0.hsrsouo.mongodb.net/')  # Replace with your MongoDB connection string
# print('this is client')
# print(client)
db = client['mytrip']  # Replace 'your_database' with your database name
# print('this is db')
# print(db)
collection = db['flask']  # Replace 'your_collection' with your collection name
# print('this is collection')
# print(collection)

answers = []
result_list = []

@app.route('/login', methods=['POST'])
def index():
    # Perform MongoDB operations here using 'collection'
    if request.method == 'POST':
        data = request.json  # Get the JSON data sent from React Native
        name = data.get('name')
        

        # Update MongoDB with the received data
        # For example, insert data into a collection

        # collection.delete_one({'name': name, 'age': age})
        
        return 'Data received and updated in MongoDB!'

@app.route('/recommend', methods=['POST'])
def recommend_algo():
    answers = request.get_json()
    print(answers)

    df = pd.read_csv('trip.csv')


    location = df["Location"].tolist()
    age = df["Age"].tolist()
    shopping = df["Shopping"].tolist()
    budget = df["Budget"].tolist()
    shopping = df["Shopping"].tolist()
    city = df["City"].tolist()
    food = df["Food"].tolist()
    hot = df["Hot"].tolist()
    siteseeing = df["Siteseeing"].tolist()
    popular = df["Popular"].tolist()
    alone = df["Alone"].tolist()
    friends = df["Friends"].tolist()
    family = df["Family"].tolist()
    lover = df["Lover"].tolist()
    history = df["History"].tolist()
    transportation = df["Transporation"].tolist()


    sum = [0] * (11)

    for i in range(len(answers)):
        for j in range(len(answers[i])):

            #Question 1
            if i == 0:
                print("Picking an age: ")
                if answers[0][0] == 1:
                    print("0 ~ 20")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[0][1] == 1:
                    print("20 ~ 30")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[0][2] == 1:
                    print("30 ~ 40")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[0][3] == 1:
                    print("40 ~ 50")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[0][4] == 1:
                    print("50 ~ 60")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0                            
                if answers[0][5] == 1:
                    print("60 ~ ")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            if i == 1:
                print("Budget")
                if answers[1][0] == 1:
                    print("0 ~ 500")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[1][1] == 1:
                    print("500 ~ 1000")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[1][2] == 1:
                    print("1000 ~ 1500")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[1][3] == 1:
                    print("1500 ~")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            if i == 2:
                print("Gender")
                if answers[2][0] == 1:
                    print("Boy")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[2][1] == 1:
                    print("Girl")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            if i == 3:
                print("Who are you going with?")
                if answers[3][0] == 1:
                    print("Alone")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[3][1] == 1:
                    print("With Friends")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[3][2] == 1:
                    print("With Family")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[3][3] == 1:
                    print("With Lover")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            if i == 4:
                print("Who are you going with?")
                if answers[4][0] == 1:
                    print("Alone")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[4][1] == 1:
                    print("With Friends")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            if i == 5:
                print("Weather?")
                if answers[5][0] == 1:
                    print("Tropical")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[5][1] == 1:
                    print("Cool")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0            
            if i == 6:
                print("Which Environment?")
                if answers[6][0] == 1:
                    print("The City")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[6][1] == 1:
                    print("Nature")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            if i == 7:
                print("Tourism or Vacation?")
                if answers[7][0] == 1:
                    print("Tourism")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[7][1] == 1:
                    print("Vacation")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            if i == 8:
                print("Bustling ?")
                if answers[8][0] == 1:
                    print("Bustling")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[8][1] == 1:
                    print("Not Bustling")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            if i == 9:
                print("Is transporation important?")
                if answers[9][0] == 1:
                    print("Yes")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[9][1] == 1:
                    print("No")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            
            if i == 10:
                print("Historical/Cultural?")
                if answers[10][0] == 1:
                    print("Yes")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[10][1] == 1:
                    print("No")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            if i == 11:
                print("Activity?")
                if answers[11][0] == 1:
                    print("Yes")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[11][1] == 1:
                    print("No")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
            if i == 12:
                print("Shopping?")
                if answers[12][0] == 1:
                    print("Yes")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
                if answers[12][1] == 1:
                    print("No")
                    for k in range(len(location)):
                        if k < len(sum):
                            sum[k] += 0
    
    

    return "Returning a recommendation"

@app.route('/result', methods=['GET'])
def get_data():

    result_list = ['Osaka', 'Danang', 'Hong Kong']

    return jsonify(result_list)

@app.route('/userReviews', methods=['POST'])
def get_reviews():
    data = request.get_json()
    location_title = data.get('where')  # Assuming location title is passed in the request
    print(location_title)
    # Query MongoDB for documents where the location_title field exists and is not empty
    reviews = collection.find({ f"{location_title}": { "$exists": True, "$ne": "" } })
    
    review_list = []  # Convert MongoDB cursor to a list of reviews
    for review in reviews:
        review_list.append({
            'name': review['name'],
            'review': review[f"{location_title}"],
            'star': review['star'],
            'profile_image': review['profile_image'],
            'wish_place': review['wish_places']
        })
        print("New New Pikachu")
        print("This is the return ldcdfdfist")
        print(review_list)

    return jsonify(review_list)
@app.route('/reviewSubmit', methods=['POST'])
def submit_review():
    user_review = request.get_json()

    username = user_review.get('name')
    star = user_review.get('star')
   # Get the location title as the key
    location_review = list(user_review.keys())[1]  # Assuming location.title is the 4th key

    review = user_review.get(location_review)  # Fetch the review text using location title as key

     # Check if the username exists in the collection
    existing_user = collection.find_one({'name': username})   
    if existing_user:
        # Update the existing document with the review field
        collection.update_one(
            {'_id': existing_user['_id']},
            {'$set': {location_review: review, 'star': star}}
        )
        return jsonify({'message': 'Review updawted successfully'})
    else:
        return jsonify({'message': 'User not found'})

@app.route('/wishlist', methods=['POST'])
def get_wishlist():
    user_review = request.get_json()

    username = user_review.get('name')
    wishlist = user_review.get('wishlist')

    print("This is the wishlist")
    print(wishlist)


     # Check if the username exists in the collection
    existing_user = collection.find_one({'name': username})   
    if existing_user:
        # Update the existing document with the review field
        collection.update_one(
            {'_id': existing_user['_id']},
            {'$set': {'wish_places': wishlist}}
        )
        return jsonify({'message': 'Review updawted successfully'})
    else:
        return jsonify({'message': 'User not found'})
    
@app.route('/user', methods=['POST'])
def receive_token():
    if request.method == 'POST':
        data = request.get_json()
        grant_type = data.get('grant_type')
        client_id = data.get('client_id')
        redirect_uri = data.get('redirect_uri')
        code = data.get('code')

        print(data)
        grant_type = data['grant_type']
        client_id = data['client_id']
        redirect_uri = data['redirect_uri']
        code = data['code']
        print(grant_type)
        
        # Perform actions with the received access token (e.g., store it in the database)
        # Example: Store the access token in the database
        # Your code here...

        token_response = requests.post(
            f'https://kauth.kakao.com/oauth/token',
            data={
                'grant_type': 'authorization_code',
                'client_id': client_id,
                'redirect_uri': redirect_uri,
                'code': code
            },
            headers={"content-type": "application/x-www-form-urlencoded"}
        )

        kakao_token = token_response.json()
        print(kakao_token)

        headers= {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'no-cache',
            'Authorization': 'Bearer ' + str(kakao_token['access_token'])
        }


        user_url = "https://kapi.kakao.com/v2/user/me"

        response = requests.request("GET", user_url, headers=headers)
        print("This is the response")
        print(response.text)


        print(type(response.text))

        json_response = json.loads(response.text)

        app_username = json_response['properties']['nickname']
        app_profile_pic = json_response['properties']['profile_image']

        print(app_profile_pic)
        
        # Check if the username exists in the collection
        existing_user = collection.find_one({'name': app_username})

        # Check if the profile pic exists in the collection
        existing_profile_pic = collection.find_one({'profile_image': app_profile_pic})

        # If either the username or profile pic doesn't exist, add them to the collection
        if not existing_user and not existing_profile_pic:
            collection.insert_one({'name': app_username, 'profile_image': app_profile_pic, 'wish_places': '', 'favorite_places': '' })
            print(f"Added {app_username} and {app_profile_pic} to the collection.")
            existing_user = collection.find_one({'name': app_username})
        else :
            existing_user = collection.find_one({'name': app_username})
            print("The user already exists, we will give you the user information")

        print(type(existing_user))
        print(existing_user['name'])
        print(existing_user['profile_image'])
        print(existing_user['wish_places'])
        print(existing_user['favorite_places'])

        data_from_db = []
        data_from_db.append(existing_user['name'])
        data_from_db.append(existing_user['profile_image'])
        data_from_db.append(existing_user['wish_places'])
        data_from_db.append(existing_user['favorite_places'])

        return jsonify(data_from_db)
    

@app.route('/', methods=['GET'])
def hello():
    # Your data (example)
    data = {
        'message': 'Hello, this is a Flask app!',
        'status': 'success'
    }
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)