import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

#Load dataset
df = pd.read_csv("data/users.csv")

#Feature selection (remove non-numeric)
features = df.drop(['user_id', 'location'], axis=1)

#Feature weighting
features['sports'] *= 2
features['tech'] *= 1.5
features['fitness'] *= 1.2

#Similarity matrix
similarity = cosine_similarity(features)


#Function to calculate common interests
def common_interests(u1, u2):
    return sum(features.iloc[u1] & features.iloc[u2])


#Main recommendation function
def recommend(user_id, top_n=5):

    #Edge case
    if user_id not in df['user_id'].values:
        return "User not found"

    #Get user location
    user_loc = df[df['user_id'] == user_id]['location'].values[0]

    similarity_scores = similarity[user_id - 1]

    final_scores = []

    for i, score in enumerate(similarity_scores):

        if i != user_id - 1:

            #Location filter
            if df.iloc[i]['location'] == user_loc:

                common = common_interests(user_id - 1, i)

                #Hybrid scoring
                final_score = (0.7 * score) + (0.3 * common)

                final_scores.append((i, final_score))

    #Sort based on final score
    sorted_users = sorted(final_scores, key=lambda x: x[1], reverse=True)

    #Top N users
    top_users = sorted_users[:top_n]

    #Convert index to user_id
    recommended_users = [i[0] + 1 for i in top_users]

    return recommended_users


#Test
if __name__ == "__main__":
    print("Recommendations for User 1:", recommend(1))
