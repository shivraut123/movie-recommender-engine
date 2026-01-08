from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # Import Security Tool
import pandas as pd
import os
from recommender import MovieRecommender

app = FastAPI()

# --- SECURITY FIX START ---
# This block tells the server to allow requests from your React App
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (Safe for local development)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
# --- SECURITY FIX END ---

# Global variables
movies = None
recommender = None

# Load Data and AI Model on Startup
data_path = './data/movies.csv'

if os.path.exists(data_path):
    movies = pd.read_csv(data_path)
    # Initialize the AI
    recommender = MovieRecommender(movies)
    print("AI Model Loaded Successfully!")
else:
    print("ERROR: movies.csv not found. Please upload data.")
    movies = pd.DataFrame()

@app.get("/")
def read_root():
    return {"message": "Movie Recommender API is running!"}

@app.get("/movies")
def get_movies():
    # Return first 20 movies so user can pick one
    if movies is None or movies.empty:
        return []
    return movies.head(20).to_dict(orient='records')

@app.get("/recommend/{title}")
def recommend_movies(title: str):
    if recommender is None:
         raise HTTPException(status_code=500, detail="Model not loaded")
    
    results = recommender.get_recommendations(title)
    
    if not results:
        raise HTTPException(status_code=404, detail="Movie not found")
        
    return results