from sentence_transformers import SentenceTransformer, util

class SentenceEmbeddings:
    def __init__(self, model_name='all-mpnet-base-v2'):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, sentences):
        return self.model.encode(sentences, convert_to_tensor=True)

    def compute_similarity(self, embedding1, embedding2):
        return util.pytorch_cos_sim(embedding1, embedding2).item()

    def compare_sentences(self, sentence1, sentence2):
        embeddings = self.generate_embeddings([sentence1, sentence2])
        similarity = self.compute_similarity(embeddings[0], embeddings[1])
        return similarity