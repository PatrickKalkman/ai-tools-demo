import string
from collections import Counter
from .constants import COMMON_WORDS_BLACKLIST
from .data_types import WordCounts

def word_counter(script: str, min_count_threshold: int = 10) -> WordCounts:
    # Remove punctuation and make all words lowercase
    translator = str.maketrans('', '', string.punctuation)
    words = script.translate(translator).lower().split()

    # Filter out common words
    filtered_words = [word for word in words if word not in COMMON_WORDS_BLACKLIST]

    # Count word frequencies
    word_counts = Counter(filtered_words)

    # Filter out words with count less than min_count_threshold
    filtered_word_counts = {word: count for word, count in word_counts.items() if count > min_count_threshold}

    # Sort words by count in descending order
    sorted_word_counts = dict(sorted(filtered_word_counts.items(), key=lambda item: item[1], reverse=True))

    return WordCounts(count_to_word_map=sorted_word_counts)
