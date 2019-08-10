# Dependencies
import joblib
import pandas as pd
from flask import Flask, jsonify, request

import sys
sys.path.append('/app')

# Your API definition
app = Flask(__name__)


#@app.route('/top_trend', methods=['GET'])
#def topTrend():
#    top_rating = df_rating.nlargest(20, ['rating', 'timestamp'])
#    top_rating_list = top_rating['movieId'].astype(str).tolist()

#    df_movie['id'] = df_movie['id'].astype(str)
#    top_trend_movies = df_movie[df_movie['id'].isin(top_rating_list)]
#    return top_trend_movies.to_json()
@app.route('/get_title', methods=['GET'])
def getTitle():
    return "Project 3 Computer Vision detects weapon"

if __name__ == '__main__':
    
    # content-based filtering
    # smd, cosine_sim = cb_filter(df_movie, links_small, credits, keywords)
    #smd = joblib.load("./smd.pkl")
    #cosine_sim = joblib.load("./cosine_sim.pkl")
    
    # svd, id_map = collab_filter(df_movie, df_rating, links_small, credits, keywords, smd)
    #svd = joblib.load("./svd.pkl")
    #id_map = joblib.load("./id_map.pkl")

    #smd = smd.reset_index()
    #titles = smd['title']
    #indices = pd.Series(smd.index, index=smd['title'])

    #print(hybrid(1, 'Avatar'))
    app.run(debug=True, host='0.0.0.0')