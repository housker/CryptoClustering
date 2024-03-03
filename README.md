# Columbia AI Module 11 Challenge: CryptoClustering Unsupervised

## Requirements

### Find the Best Value for k Using the Original Scaled DataFrame (15 points)
- [X] Code the elbow method algorithm to find the best value for k. Use a range from 1 to 11. (5 points)
- [X] Visually identify the optimal value for k by plotting a line chart of all the inertia values computed with the different values of k. (5 points)
- [X] Answer the following question: What’s the best value for k? (5 points)

### Cluster Cryptocurrencies with K-Means Using the Original Scaled Data (10 points)
- [X] Initialize the K-means model with four clusters by using the best value for k. (1 point)
- [X] Fit the K-means model by using the original data. (1 point)
- [X] Predict the clusters for grouping the cryptocurrencies by using the original data. Review the resulting array of cluster values. (3 points)
- [X] Create a copy of the original data, and then add a new column of the predicted clusters. (1 point)
- [X] Using pandas’ plot, create a scatter plot by setting x="price_change_percentage_24h" and y="price_change_percentage_7d". (4 points)

### Optimize the Clusters with Principal Component Analysis (10 points)
- [X] Create a PCA model instance, and set n_components=3. (1 point)
- [X] Use the PCA model to reduce the features to three principal components, then review the first five rows of the DataFrame. (2 points)
- [X] Get the explained variance to determine how much information can be attributed to each principal component. (2 points)
- [X] Answer the following question: What’s the total explained variance of the three principal components? (3 points)
- [X] Create a new DataFrame with the PCA data. Be sure to set the coin_id index from the original DataFrame as the index for the new DataFrame. Review the resulting DataFrame. (2 points)

### Find the Best Value for k by Using the PCA Data (10 points)
- [X] Code the elbow method algorithm, and use the PCA data to find the best value for k. Use a range from 1 to 11. (2 points)
- [X] Visually identify the optimal value for k by plotting a line chart of all the inertia values computed with the different values of k. (5 points)
- [X] Answer the following questions: What’s the best value for k when using the PCA data? Does it differ from the best value for k that you found by using the original data? (3 points)

### Cluster the Cryptocurrencies with K-Means by Using the PCA Data (10 points)
- [X] Initialize the K-means model with four clusters by using the best value for k. (1 point)
- [X] Fit the K-means model by using the PCA data. (1 point)
- [X] Predict the clusters for grouping the cryptocurrencies by using the PCA data. Review the resulting array of cluster values. (3 points)
- [X] Create a copy of the DataFrame with the PCA data, and then add a new column to store the predicted clusters. (1 point)
- [X] Using pandas’ plot, create a scatter plot by setting x="PC1" and y="PC2". (4 points)

### Determine the Weights of Each Feature on Each Principal Component (15 points)
- [X] Create a DataFrame that shows the weights of each feature (column) for each principal component by using the columns from the original scaled DataFrame as the index. (10 points)
- [X] Answer the following question: Which features have the strongest positive or negative influence on each component? (5 points)

### Coding Conventions and Formatting (10 points)
- [X] Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. (3 points)
- [X] Name functions and variables with lowercase characters, with words separated by underscores. (2 points)
- [X] Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. (3 points)
- [X] Use concise logic and creative engineering where possible. (2 points)

### Deployment and Submission (10 points)
- [X] Submit a link to a GitHub repository that’s cloned to your local machine and that contains your files. (4 points)
- [X] Use the command line to add your files to the repository. (3 points)
- [X] Include appropriate commit messages in your files. (3 points)

### Code Comments (10 points)
- [X] Be well commented with concise, relevant notes that other developers can understand. (10 points)