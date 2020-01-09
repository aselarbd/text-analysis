from sklearn.cluster import AgglomerativeClustering


def Cluster(noOfClusters, headings, descriptions, corpus):
    clusters = [[] for i in range(noOfClusters)]

    clusteringModel = AgglomerativeClustering(n_clusters=noOfClusters)
    clusteringModel.fit(corpus)
    clusterAssignment = clusteringModel.labels_

    for ID, clusterId in enumerate(clusterAssignment):
        clusters[clusterId].append({"heading": headings[ID][1].strip(),
                                    "text": descriptions[ID][1].strip()})
    return clusters
