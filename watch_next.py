# importing spacy
import spacy

# loading the english model to find our similarities
nlp = spacy.load("en_core_web_md")


# creating my function to determine similar movie with 'description' argument
def find_similar_movie(description):

    # convert the description variable to a spaCy doc
    description_doc = nlp(description)

    # empty movies list
    movies = []

    # open file and read the movies from movie text file into a list of tuples (empty 'movies' list)
    with open("movies.txt", "r") as file:
        for line in file:
            title, desc = line.strip().split(":")

            # appending the title and description of the movies into the empty movie list as tuples
            movies.append((title, nlp(desc)))

    # counter control variable and similar movie empty string variable
    max_similarity = 0
    similar_movie = ""

    # for loop to iterate through the 'movies' list
    for movie in movies:

        # similarity score calculated using the spaCy similarity method, the similarities between the description (in this case the hulk movie) and the description of movies in the list, using slicing methods
        similarity = description_doc.similarity(movie[1])

        # if the similarity score is greater than the current maximum similarity (in this case 0)
        if similarity > max_similarity:

            # the max similarity is replaced with the new similarity score
            max_similarity = similarity

            # similar movie variable is updated with the title of the similar movie
            similar_movie = movie[0:]

    # similar movie is returned
    return similar_movie


# hulk movie description
hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

print(find_similar_movie(hulk))
