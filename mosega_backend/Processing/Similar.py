import scipy.spatial


def Similar(query, clauses, headings, descriptions, corpus, embedder):
    result_list = []

    queries = [query]
    query_embeddings = embedder.encode(queries)

    for query, query_embedding in zip(queries, query_embeddings):
        distances = scipy.spatial.distance.cdist([query_embedding], corpus, "cosine")[0]

        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

        for ID, distance in results[0:clauses]:
            result_list.append({"heading": headings[ID][1].strip(),
                               "text": descriptions[ID][1].strip(),
                               "accuracy": 1 - distance})
    return result_list
