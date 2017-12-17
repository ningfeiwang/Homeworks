
import sklearn.cluster as cluster
import numpy, sys
import networkx
import matplotlib.pyplot as plt


# main procedure
if __name__ == "__main__":

    ### clustering algorithm names and parameter settings
    clustering_configs = [
        ### K-Means
        ['KMeans', {'n_clusters' : 5}],
        ### Ward
        ['AgglomerativeClustering', {
                    'n_clusters' : 5,
                    'linkage' : 'ward'
                    }],
        ### DBSCAN
        ['DBSCAN', {'eps' : 0.15}]
    ]

    ### load data from standard input
    X = []
    for line in sys.stdin:
        x1, x2 = line.strip().split()
        X.append([float(x1), float(x2)])
    X = numpy.array(X)

    ### perform clustering and collect results
    ### hint:
    ### (1) import a class by string by "getattr"
    ### (2) arguments unpacking: pass arguments as a dictionary to create an instance

    clustering_results = {}

    for alg_name, alg_params in clustering_configs:

        ###! finish the following statments
        class_ = getattr(cluster, alg_name)
        if alg_name == 'KMeans':
            instance_= class_(n_clusters = alg_params.get('n_clusters'))

        if alg_name == 'AgglomerativeClustering':
            instance_= class_(n_clusters = alg_params.get('n_clusters'), linkage = alg_params.get('linkage'))

        if alg_name == 'DBSCAN':
            instance_ = class_(eps = alg_params.get('eps'))   

        # print clustering_results
        ### perform clustering and collect results
        ### hint: use fit_predict function


        ###! finish the following statements
        # clustering_results[alg_name] = instance_
        clustering_results[alg_name] = instance_.fit_predict(X)

    ### number of data points
    n = X.shape[0]

    ### for each pair of points, they belong to the same cluster only if all algorithms agree
    ### hint: create a graph, each data point corresponds to a node, two nodes are connected
    ###     if they belong to the same cluster

    G = networkx.Graph()

    for i in xrange(n):
        for j in xrange(i+1, n):
            count = 0
            for results in clustering_results.values():
                ###! your code here
                if results[i] == results[j]:
                    count += 1
                    # print count
            if count == len(clustering_results):
                ###! your code here
                G.add_edge(i, j)


    ### assgin cluster labels to data points
    ### hint: each connected component in G represents a cluster
    class_label = 0
    clustering_results['Meta'] = numpy.zeros((n,))
    # print networkx.connected_components(G)
    for connected_component in networkx.connected_components(G):
        ###! your code here
        # print connected_component
        for k in connected_component:
            clustering_results['Meta'][k] = class_label
        class_label += 1
    # print class_label

    # plot the results
    plt.subplot(221)
    plt.scatter(X[:, 0], X[:, 1], c=clustering_results['KMeans'])
    plt.title("KMeans")

    plt.subplot(222)
    plt.scatter(X[:, 0], X[:, 1], c=clustering_results['AgglomerativeClustering'])
    plt.title("Ward")

    plt.subplot(223)
    plt.scatter(X[:, 0], X[:, 1], c=clustering_results['DBSCAN'])
    plt.title("DBSCAN")

    plt.subplot(224)
    plt.scatter(X[:, 0], X[:, 1], c=clustering_results['Meta'])
    plt.title("Meta")

    plt.show()
