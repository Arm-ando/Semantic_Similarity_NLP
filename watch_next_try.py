import spacy


def find_similar_movie(description):

    nlp = spacy.load('en_core_web_md')

    description_doc = nlp(description)

    movie_list = []

    with open('movies.txt', 'r') as file:
        for line in file:
            movie, desc = line.strip().split(":")
            movie_list.append((movie, desc))


    similarity_scores = []

    for movies in movie_list:
        movie_doc = nlp(movie[1])
        score = 0

        for token in description_doc:
            for token2 in movie_doc:
                score += token.similarity(token2)

            similarity_scores.append((movie[0], score))

        similarity_scores.sort(key=lambda x: x[1], reverse=True)

        print(similarity_scores[0][0])


hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."


find_similar_movie(hulk)
