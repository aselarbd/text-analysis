from sklearn.cluster import AgglomerativeClustering
import Constants


def Cluster(no_of_clusters, headings, descriptions, corpus):
    clusters = [[] for i in range(no_of_clusters)]

    clustering_model = AgglomerativeClustering(n_clusters=no_of_clusters)
    clustering_model.fit(corpus)
    cluster_assignment = clustering_model.labels_

    for ID, clusterId in enumerate(cluster_assignment):
        clusters[clusterId].append({Constants.HEADING: headings[ID][1].strip(),
                                    Constants.TEXT: descriptions[ID][1].strip()})
    return clusters
