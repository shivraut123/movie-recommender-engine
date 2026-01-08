# 🎬 AI Movie Recommender Engine

A Full-Stack Machine Learning application that suggests movies based on content similarity. Built for the purpose of demonstrating Full Stack Engineering (React + FastAPI) combined with Data Science (TF-IDF Vectorization).

![Project Status](https://img.shields.io/badge/Status-Complete-green)
![Tech Stack](https://img.shields.io/badge/Stack-React%20|%20FastAPI%20|%20ScikitLearn-blue)

## 📌 Project Overview
This project solves the **"Cold Start Problem"** in recommendation systems. Instead of relying on user history (which doesn't exist for new users), this engine analyzes movie metadata (genres, descriptions) to find mathematical similarities between titles.

## 🎥 Project Demo
[![Watch the video](https://img.youtube.com/vi/ale9w5o-90k/maxresdefault.jpg)](https://youtu.be/ale9w5o-90k)

**Key Technical Features:**
* **TF-IDF Vectorization:** Converts text-based movie genres into high-dimensional vectors.
* **Cosine Similarity:** Calculates the angular distance between movie vectors to determine relevance.
* **Real-time API:** A FastAPI backend serves recommendations in <100ms.
* **Interactive UI:** A React frontend (Vite) provides instant feedback and dynamic state management.

## 🛠️ Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend** | React (Vite) | User Interface & State Management |
| **Backend** | FastAPI (Python) | REST API & ML Model Serving |
| **ML Engine** | Scikit-Learn | Vectorization & Similarity Math |
| **Data** | Pandas | Dataframe Manipulation (MovieLens Dataset) |

## 🏗️ System Architecture
The application follows a decoupled client-server architecture:

```mermaid
graph LR
    A[User / Browser] -- HTTP Request --> B[Frontend (React)]
    B -- Async API Call (Axios) --> C[Backend (FastAPI)]
    C -- Query --> D[Recommendation Engine]
    D -- Read Data --> E[(MovieLens Dataset)]
    D -- Compute TF-IDF --> D
    D -- Return Top 5 Matches --> C
    C -- JSON Response --> B
    B -- Render UI --> A

## 🚀 How to Run Locally

### Prerequisites
* Node.js (v14+)
* Python (v3.8+)

### 1. Clone the Repo
```bash
git clone [https://github.com/shivraut123/movie-recommender-engine.git](https://github.com/shivraut123/movie-recommender-engine.git)
cd movie-recommender-engine

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.