"""Count letters in phrase.

Example:
    >>> letter_counts = make_letter_counts_dict('delicious knishes')
    >>> print(letter_counts['s'])
    3
"""


def make_letter_counts_dict(phrase):
    """Return dict of letters and # of occurrences in phrase."""

    letter_counts = {}

    for letter in phrase:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    return letter_counts


letter_counts = make_letter_counts_dict('delicious knishes')
print(letter_counts)
