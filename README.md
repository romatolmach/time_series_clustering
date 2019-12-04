
# Time series clustering by sklearn trees
Solution of the problem based on algorithm from the article:**"Method for clustering of heterogeneous time series" **by Berikov Vladimir, Pestunov Igor, Gerasimov Maxim 

link (RUS) : https://cyberleninka.ru/article/n/metod-klasternogo-analiza-raznotipnyh-vremennyh-ryadov 

## Algorithm
1. For each time series Y<sub>i </sub>based on training set V<sub>i </sub> a decision tree g<sub>i </sub> is being built
1. For each decision tree g<sub>i </sub> the standard errors μ<sub>ij</sub> are calculated on training samples V<sub>j </sub>
1. For all time series, pairwise measures of the difference ρ(i, j) are calculated. The matrix M is determined.
1. Using the matrix of various differences M and the standard hierarchical clustering algorithm find time series clustrers.

## My results