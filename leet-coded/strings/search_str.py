# def suggestedProducts(products, searchWord):
#     list_final = []
#     products.sort()
    
#     for i,n in enumerate(searchWord):
#         products=[p for p in products if len(p)>i and p[i]==n]
#         list_final.append(products[:3])
#     return list_final

# products = ["mobile","mouse","moneypot","monitor","mousepad"]
# searchWord = "mouse"
# print(suggestedProducts(products,searchWord))
import collections
def topKFrequent(words, k):
    counter = collections.Counter(words)
    return sorted(counter.keys(), key = lambda x: (-counter[x],x) )

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(topKFrequent(words, k))