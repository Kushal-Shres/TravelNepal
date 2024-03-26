import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel

# ds = pd.read_csv("travel_place.csv",sep=',',header=None)
#
# print(ds)
# tf = TfidfVectorizer(analyzer='word')
# tfidf_matrix = tf.fit_transform(ds['category'])
# print(tfidf_matrix)

# cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
#
# results = {}
#
# for idx, row in ds.iterrows():
#     similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
#     similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]
#
#     # First item is the item itself, so remove it.
#     # Each dictionary entry is like: [(1,2), (3,4)], with each tuple being (score, item_id)
#     results[row['id']] = similar_items[1:]
#
# print('done!')
