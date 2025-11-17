def calculate_semantic_similarity(output_a, output_b):
    # Function to calculate semantic similarity between two outputs
    from sentence_transformers import SentenceTransformer, util

    model = SentenceTransformer("all-mpnet-base-v2")
    embeddings_a = model.encode(output_a, convert_to_tensor=True)
    embeddings_b = model.encode(output_b, convert_to_tensor=True)

    cosine_similarity = util.pytorch_cos_sim(embeddings_a, embeddings_b)
    return cosine_similarity.item()


def calculate_lexical_distance(output_a, output_b):
    # Function to calculate lexical distance between two outputs
    from nltk.metrics import edit_distance

    return edit_distance(output_a, output_b)


def calculate_topic_shift(original_output, new_output):
    # Function to calculate topic shift using LDA or clustering
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.decomposition import LatentDirichletAllocation

    vectorizer = CountVectorizer()
    doc_term_matrix = vectorizer.fit_transform([original_output, new_output])
    lda = LatentDirichletAllocation(n_components=2, random_state=0)
    lda.fit(doc_term_matrix)

    return lda.components_


def calculate_named_entity_drift(original_output, new_output):
    # Function to calculate named entity drift
    import spacy

    nlp = spacy.load("en_core_web_sm")
    original_doc = nlp(original_output)
    new_doc = nlp(new_output)

    original_entities = {ent.text for ent in original_doc.ents}
    new_entities = {ent.text for ent in new_doc.ents}

    drift = new_entities - original_entities
    return drift


def calculate_iteration_cost(iterations):
    # Function to calculate the cost of iterations
    total_tokens = sum(len(iteration.split()) for iteration in iterations)
    return total_tokens, len(
        iterations
    )  # returns total tokens and number of iterations


def calculate_metrics(results: list) -> dict:
    """
    Calculates a dictionary of metrics from the results of the iterative prompting.

    Args:
        results (list): A list of outputs from each iteration.

    Returns:
        dict: A dictionary of metrics.
    """
    if not results:
        return {}

    first_result = results[0]
    metrics_over_time = []
    for i in range(len(results)):
        iteration_metrics = {
            "iteration": i + 1,
            "semantic_similarity": calculate_semantic_similarity(
                first_result, results[i]
            ),
            "lexical_distance": calculate_lexical_distance(first_result, results[i]),
        }
        metrics_over_time.append(iteration_metrics)

    final_metrics = {
        "metrics_over_time": metrics_over_time,
        "topic_shift": calculate_topic_shift(first_result, results[-1]).tolist(),
        "named_entity_drift": list(
            calculate_named_entity_drift(first_result, results[-1])
        ),
        "iteration_cost": calculate_iteration_cost(results),
    }

    return final_metrics
