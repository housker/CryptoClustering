import re
import requests
import subprocess

def search_file(file, pattern):
    content = open(file).read()
    return bool(re.search(pattern, content, re.MULTILINE | re.DOTALL))

# Note: the search_git tests will not necessarily pass on machines that pull this code from remote
def search_git(process, pattern):
       gitlog = subprocess.run(['git', process], capture_output=True, text=True).stdout
       return bool(re.search(pattern, gitlog))


### Find the Best Value for k Using the Original Scaled DataFrame (15 points)
def test_bestk_original():
    assert search_file("Crypto_Clustering.ipynb", rf"k = list\(range\(1, 11\)\).*for i in k:.*k_model = KMeans\(n_clusters=i, n_init='auto', random_state=1\).*k_model\.fit\(df\).*inertia.append\(k_model\.inertia_\)") == True, "Code the elbow method algorithm to find the best value for k. Use a range from 1 to 11. (5 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"df_elbow\.plot\.line\(x=\\\"k\\\",.*y=\\\"inertia\\\",.*title=\\\"Elbow Curve\\\",.*xticks=k\)") == True, "Visually identify the optimal value for k by plotting a line chart of all the inertia values computed with the different values of k. (5 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"What is the best value for `k`?.*\*\*Answer:\*\* 4") == True, "Answer the following question: What’s the best value for k? (5 points)"

### Cluster Cryptocurrencies with K-Means Using the Original Scaled Data (10 points)
def test_clustering_original():
    assert search_file("Crypto_Clustering.ipynb", rf"model = KMeans\(n_clusters=k, n_init=\'auto\'\)") == True, "Initialize the K-means model with four clusters by using the best value for k. (1 point)"

    assert search_file("Crypto_Clustering.ipynb", rf"model\.fit\(df\)") == True, "Fit the K-means model by using the original data. (1 point)"

    assert search_file("Crypto_Clustering.ipynb", rf"prediction = model\.predict\(df\).*print\(prediction\)") == True, "Predict the clusters for grouping the cryptocurrencies by using the original data. Review the resulting array of cluster values. (3 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"predictions_df = df\.copy\(\).*df = predictions_df\.assign\(crypto_cluster=prediction\)") == True, "Create a copy of the original data, and then add a new column of the predicted clusters. (1 point)"

    assert search_file("Crypto_Clustering.ipynb", rf"predictions_df\.plot\.scatter\(.*x=x,.*y=y,.*c=\\\"crypto_cluster\\\",.*colormap=\\\"rainbow\\\".*\).*kmeans_cluster\(crypto_df, 4, \\\"price_change_percentage_24h\\\", \\\"price_change_percentage_7d\\\"\)") == True, "Using pandas’ plot, create a scatter plot by setting x='price_change_percentage_24h' and y='price_change_percentage_7d'. (4 points)"

### Optimize the Clusters with Principal Component Analysis (10 points)
def test_pca():
    assert search_file("Crypto_Clustering.ipynb", rf"pca = PCA\(n_components=3\)") == True, "Create a PCA model instance, and set n_components=3. (1 point)"

    assert search_file("Crypto_Clustering.ipynb", rf"crypto_pca = pca\.fit_transform\(crypto_df\)") == True, "Use the PCA model to reduce the features to three principal components, then review the first five rows of the DataFrame. (2 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"pca\.explained_variance_ratio_") == True, "Get the explained variance to determine how much information can be attributed to each principal component. (2 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"What is the total explained variance of the three principal components?.*\*\*Answer:\*\* 89\.5%") == True, "Answer the following question: What’s the total explained variance of the three principal components? (3 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"crypto_pca_df = pd\.DataFrame\(.*crypto_pca,.*columns=\[\\\"PCA1\\\", \\\"PCA2\\\", \\\"PCA3\\\"\],.*index=market_data_df\.index.*\).*crypto_pca_df\.head\(10\)") == True, "Create a new DataFrame with the PCA data. Be sure to set the coin_id index from the original DataFrame as the index for the new DataFrame. Review the resulting DataFrame. (2 points)"

### Find the Best Value for k by Using the PCA Data (10 points)
def test_bestk_pca():
    assert search_file("Crypto_Clustering.ipynb", rf"pca_df_elbow = get_k_elbow\(crypto_pca_df\)") == True, "Code the elbow method algorithm, and use the PCA data to find the best value for k. Use a range from 1 to 11. (2 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"pca_df_elbow = get_k_elbow\(crypto_pca_df\)") == True, "Visually identify the optimal value for k by plotting a line chart of all the inertia values computed with the different values of k. (5 points)"
    
    assert search_file("Crypto_Clustering.ipynb", rf"What is the best value for `k` when using the PCA data?.*\*\*Answer:\*\* 4.*\*\*Question:\*\* Does it differ from the best k value found using the original data?.*\*\*Answer:\*\* No") == True, "Answer the following questions: What’s the best value for k when using the PCA data? Does it differ from the best value for k that you found by using the original data? (3 points)"

### Cluster the Cryptocurrencies with K-Means by Using the PCA Data (10 points)
def test_clustering_pca():
    assert search_file("Crypto_Clustering.ipynb", rf"kmeans_cluster\(crypto_pca_df, 4,") == True, "Initialize the K-means model with four clusters by using the best value for k. (1 point)"

    assert search_file("Crypto_Clustering.ipynb", rf"kmeans_cluster\(crypto_pca_df,") == True, "Fit the K-means model by using the PCA data. (1 point)"

    assert search_file("Crypto_Clustering.ipynb", rf"kmeans_cluster\(crypto_pca_df, 4, \\\"PCA1\\\", \\\"PCA2\\\"\)") == True, "Predict the clusters for grouping the cryptocurrencies by using the PCA data. Review the resulting array of cluster values. (3 points))"

    assert search_file("Crypto_Clustering.ipynb", rf"kmeans_cluster\(crypto_pca_df, 4, \\\"PCA1\\\", \\\"PCA2\\\"\)") == True, "Create a copy of the DataFrame with the PCA data, and then add a new column to store the predicted clusters. (1 point)"

    assert search_file("Crypto_Clustering.ipynb", rf"kmeans_cluster\(crypto_pca_df, 4, \\\"PCA1\\\", \\\"PCA2\\\"\)") == True, "Using pandas’ plot, create a scatter plot by setting x='PC1' and y='PC2'. (4 points)"

### Determine the Weights of Each Feature on Each Principal Component (15 points)
def test_weights():
    assert search_file("Crypto_Clustering.ipynb", rf"pd.DataFrame\(pca.components_.T, columns=crypto_pca_df.columns, index=crypto_df\.columns\)") == True, "Create a DataFrame that shows the weights of each feature (column) for each principal component by using the columns from the original scaled DataFrame as the index. (10 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"`price_change_percentage_200d` and `price_change_percentage_1y` have the strongest influence on PCA1.* strongest influence on PCA3\. All of these are positive\. The negative ones have less weight\.") == True, "Answer the following question: Which features have the strongest positive or negative influence on each component? (5 points)"

### Coding Conventions and Formatting (10 points)
def test_conventions():
    assert search_file("Crypto_Clustering.ipynb", rf"# Import required libraries and dependencies.*import pandas as pd.*from sklearn.cluster import KMeans.*from sklearn.decomposition import PCA.*from sklearn.preprocessing import StandardScaler(?!.*import).*$") == True, "Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. (3 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"[^[a-z]+(?:_[a-z]+)*] =|\(\):") == False, "Name functions and variables with lowercase characters, with words separated by underscores. (2 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"def get_k_elbow\(df\):.*def kmeans_cluster\(df, k, x, y\):") == True, "Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. (3 points)"

    assert search_file("Crypto_Clustering.ipynb", rf"\.columns.*\.index.*get_k_elbow\(.*\).*kmeans_cluster\(.*\)") == True, "Use concise logic and creative engineering where possible. (2 points)"

### Deployment and Submission (10 points)
def submission():
    assert requests.get("https://github.com/housker/CryptoClustering").status_code == 200, "Submit a link to a GitHub repository that’s cloned to your local machine and that contains your files. (4 points))"

    assert search_git("reflog", rf"commit.*checkout") == True, "Use the command line to add your files to the repository. (3 points)"

    assert search_git("log", rf"chore: setup") == True, "Include appropriate commit messages in your files. (3 points)"

### Code Comments (10 points)
def test_comments():
    assert search_file("Crypto_Clustering.ipynb", rf"# I extracted the following steps into a function `kmeans_cluster`") == True, "Be well commented with concise, relevant notes that other developers can understand. (10 points)"
