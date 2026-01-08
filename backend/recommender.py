import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# This class handles the Machine Learning logic
class MovieRecommender:
    def __init__(self, movies_df):
        self.movies_df = movies_df
        self._prepare_data()

    def _prepare_data(self):
        # 1. Create a TfidfVectorizer
        # This turns text genres (e.g., "Action|Adventure") into mathematical vectors
        tfidf = TfidfVectorizer(stop_words='english')

        # 2. Fit and Transform the data
        # We fill NaN values with empty strings to avoid errors
        self.movies_df['genres'] = self.movies_df['genres'].fillna('')
        
        # This matrix represents the "DNA" of every movie based on its genres
        self.tfidf_matrix = tfidf.fit_transform(self.movies_df['genres'])

        # 3. Compute Cosine Similarity
        # This calculates the similarity score (0 to 1) between every movie pair
        # Warning: For massive datasets, we would verify memory usage here.
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

        # Create a reverse map of indices and movie titles for fast lookups
        self.indices = pd.Series(self.movies_df.index, index=self.movies_df['title']).drop_duplicates()

    def get_recommendations(self, title, num_recommendations=5):
        # Check if movie exists
        if title not in self.indices:
            return []

        # Get the index of the movie that matches the title
        idx = self.indices[title]

        # Get the pairwise similarity scores of all movies with that movie
        sim_scores = list(enumerate(self.cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the top n most similar movies
        # We start at 1 because 0 is the movie itself
        sim_scores = sim_scores[1:num_recommendations+1]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top movies
        return self.movies_df.iloc[movie_indices][['title', 'genres']].to_dict(orient='records')