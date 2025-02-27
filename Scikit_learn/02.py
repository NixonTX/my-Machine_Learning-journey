## Handling Categorical Data - categorical data (like "cat", "dog", "bird") needs to be converted into numerical values

## Label Encoding ##
from sklearn.preprocessing import LabelEncoder

categorical_feature = ['cat', 'dog', 'dog', 'cat', 'bird']  # list of categorical values

encoder = LabelEncoder()    # to create an encoder object that will "convert categorical values into numerical labels."

encoded_feature = encoder.fit_transform(categorical_feature)    # instance of encoder

"""
.fit_transform()
   1. Finds unique categories and assigns numeric labels:
    "bird" → 0
    "cat" → 1
    "dog" → 2
   2. Replaces original values with their numeric labels.
"""

print("Encoded feature:", encoded_feature)