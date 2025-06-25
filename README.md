# MTG Commander AI

**MTG Commander AI** is a full-stack web application that allows users to describe a Commander deck using natural language and receive closely matching decklists. It leverages modern vector search techniques and large language models to bridge the gap between free-form text and structured Magic: The Gathering (MTG) deck data.

## Features

- Vector Search: Search for Commander decks based on natural language descriptions (e.g., “a mono red pirate deck”).
- AI-Generated Descriptions: Each deck is annotated using large language models for enhanced semantic matching.
- Full Stack Architecture: A Python backend and React frontend deployed on Render for a seamless user experience.

## How It Works

### 1. Data Collection

Deck data is collected using the [pyedhrec](https://pypi.org/project/pyedhrec/) library, which interfaces with the EDHREC API to scrape decklists. The initial dataset contains around 2,000 decks, each stored in a MongoDB collection.

To provide natural language context for each deck, deck descriptions were generated using Anthropic's Claude model. These AI-generated summaries are stored alongside the raw deck data in the database.

> _Note: Future improvements may include expanding the dataset via web scraping tools like Selenium._

### 2. Vector Search

Using OpenAI’s text embedding tools, the system generates vector representations of each deck description. These embeddings are stored in MongoDB alongside the original text, enabling efficient semantic search.

When a user enters a description, the backend searches for the top vector matches and returns the most relevant decklists.

### 3. Frontend and Deployment

The frontend is built with React and provides a simple interface for users to input natural language queries. It communicates with a Python server to retrieve matching decks based on vector similarity.

Both frontend and backend are deployed on [Render](https://render.com), making the application accessible online. Note that the first request may take a few moments to respond due to cold start latency.

## Live Demo

You can try out the app here:  
[**Live Demo on Render**](https://mtg-commander-ai.onrender.com)  
(*Please allow some time for the server to spin up on the first request.*)

## Project Status

This project is currently in the prototype phase. While functional, it is an early version with limited dataset size. Future development goals include:

- Expanding the dataset via broader scraping
- Improving embedding quality and performance
- Enhancing the frontend UX
- Adding support for more advanced filters and sorting

## Contributing

Pull requests are welcome. If you have ideas for improvements, data sources, or optimizations, feel free to open an issue or contribute directly.
