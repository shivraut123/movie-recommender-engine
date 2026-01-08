import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [movies, setMovies] = useState([])
  const [recommendations, setRecommendations] = useState([])
  const [selectedMovie, setSelectedMovie] = useState(null)
  const [loading, setLoading] = useState(false)

  // 1. Fetch available movies from Backend on load
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/movies')
      .then(response => {
        setMovies(response.data)
      })
      .catch(error => console.error("Error fetching movies:", error))
  }, [])

  // 2. Function to get recommendations
  const getRecommendations = (title) => {
    setLoading(true)
    setSelectedMovie(title)
    axios.get(`http://127.0.0.1:8000/recommend/${title}`)
      .then(response => {
        setRecommendations(response.data)
        setLoading(false)
      })
      .catch(error => {
        console.error("Error fetching recommendations:", error)
        setLoading(false)
      })
  }

  return (
    <div className="container">
      <header>
        <h1>🎬 Movie AI Recommender</h1>
        <p>Pick a movie you like, and our AI will suggest similar ones.</p>
      </header>

      <main>
        {/* Left Side: Movie List */}
        <section className="movie-list">
          <h2>Available Movies</h2>
          <div className="list-container">
            {movies.map((movie, index) => (
              <button 
                key={index} 
                className={`movie-btn ${selectedMovie === movie.title ? 'active' : ''}`}
                onClick={() => getRecommendations(movie.title)}
              >
                {movie.title}
              </button>
            ))}
          </div>
        </section>

        {/* Right Side: Recommendations */}
        <section className="results">
          <h2>
            {selectedMovie 
              ? `Because you liked "${selectedMovie}"...` 
              : "Select a movie to see results"}
          </h2>

          {loading && <p>Thinking...</p>}

          <div className="cards-grid">
            {recommendations.map((rec, index) => (
              <div key={index} className="movie-card">
                <h3>{rec.title}</h3>
                <span className="genres">{rec.genres.replace(/\|/g, ', ')}</span>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  )
}

export default App