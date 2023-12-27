# Semantic Similarity NLP

This was task 38 from the HyperionDev DfE funded software engineering bootcamp.

<h2>Movie Recommendation System</h2>
In this project, we have developed a movie recommendation system that suggests what to watch next based on the word vector similarity of movie descriptions. The system is implemented in a Python script named watch_next.py.

<h2>Features</h2>
<b>watch_next.py:</b> This file serves as the core of the recommendation system. It reads in a file named movies.txt, where each line contains the description of a different movie.

<h3>Movie Description Similarity:</h3> The system focuses on word vector similarity to determine which movies are most similar to a given movie description. Specifically, it addresses the scenario where a user has watched "Planet Hulk" with the description: "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

<h3>Recommendation Function:</h3> A crucial part of the system is a function that takes a movie description as a parameter and returns the title of the most similar movie. This function aids users in making informed decisions about what movie to watch next based on their interests.
