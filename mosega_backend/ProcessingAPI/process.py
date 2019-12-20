"""
This is a simple application for sentence embeddings: semantic search
We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.
This script outputs for various queries the top 5 most similar sentences in the corpus.
"""
from sentence_transformers import SentenceTransformer
import scipy.spatial
from sklearn.cluster import AgglomerativeClustering

embedder = SentenceTransformer('bert-base-nli-mean-tokens')

# Corpus with example sentences
corpus = ["""How do we collect and use information""",
          """Account Information""",
          """Information Related to Use of the Services""",
          """Location Information""",
          """Mobile Device Information""",
          """Account holders""",
          """Guest Users""",
          """Information Shared with Our Services Providers""",
          """Information Shared with Third Parties""",
          """Information Disclosed in Connection with Business Transactions""",
          """Information Disclosed for Our Protection and the Protection of Others""",
          """Information We Disclose With Your Consent or at Your Request""",
          """The Security of Your Information""",
          """Links to Other Sites""",
          """Modifying Your Information""",
          """International Transfer""",
          """Our Policy Toward Children""",
          """Changes to Privacy Policy""",
          """Questions?""",
          """Here's a link to our partner privacy policy""",
          """1\. General""",
          """2\. Personal information you may give us""",
          """3\. Legal basis for using your personal information""",
          """Our legitimate interests""",
          """4\. Cookies""",
          """Tracking cookies""",
          """Advertising cookies""",
          """5\. Disclosure of your personal information""",
          """7\. Children’s privacy""",
          """8\. Your right to information, correction, deletion and objection""",
          """9\. Amendment""",
          """Section 1: Personal Data We Process to Serve and Personalize Advertising""",
          """Personal Data We Collect About You Through Apps""",
          """Section 2: Personal Data We Process If You Visit MoPub.com""",
          """Section 3: Personal Data We Process If You Are a Publisher or Advertising""",
          """2\. PRESENTATION OF THE APPLICATION""",
          """5\. INTELLECTUAL PROPERTY""",
          """7\. DATA PROTECTION""",
          """Does Amazon.com Share the Information It Receives?""",
          """How Secure Is Information About Me?""",
          """What About Third-Party Advertisers and Links to Other Websites?""",
          """Which Information Can I Access?""",
          """Are Children Allowed to Use Amazon.com?""",
          """Conditions of Use, Notices, and Revisions""",
          """Legal Policies""",
          """Advertising & Third Party Products and Services""",
          """Legal basis for using your personal information""",
          """What Personal Information About Customers Does Amazon.com Gather?""",
          """What About Cookies?"""
          ]
corpus_embeddings = embedder.encode(corpus)

# Query sentences:
queries = ['How does Adobe use the information it collects about me, and what are the']
query_embeddings = embedder.encode(queries)

# Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
closest_n = 5
for query, query_embedding in zip(queries, query_embeddings):
    distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]

    results = zip(range(len(distances)), distances)
    results = sorted(results, key=lambda x: x[1])

    print("\n\n======================\n\n")
    print("Query:", query)
    print("\nTop 5 most similar sentences in corpus:")

    for idx, distance in results[0:closest_n]:
        print(corpus[idx].strip(), "(Score: %.4f)" % (1 - distance))

print("\n\n======================\n\n")

num_clusters = 7
clustering_model = AgglomerativeClustering(n_clusters=num_clusters)
clustering_model.fit(corpus_embeddings)
cluster_assignment = clustering_model.labels_

clustered_sentences = [[] for i in range(num_clusters)]
for sentence_id, cluster_id in enumerate(cluster_assignment):
    clustered_sentences[cluster_id].append(corpus[sentence_id])

for i, cluster in enumerate(clustered_sentences):
    print("Cluster ", i + 1)
    print(cluster)
    print("")
