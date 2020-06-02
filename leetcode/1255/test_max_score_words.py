import unittest
import logging
from typing import List
from collections import Counter


LOG = logging.getLogger(__name__)


class MaxScoreWords:
    """
    https://leetcode.com/problems/maximum-score-words-formed-by-letters/

    Given a list of words, list of single letters (might be repeating) and score of every
    character.

    Return the maximum score of any valid set of words formed by using the given letters
    (words[i] cannot be used two or more times).

    It is not necessary to use all characters in letters and each letter can only be used once.
    Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25]
    respectively.

    Example 1:

    Input:
    words = ["dog","cat","dad","good"],
    letters = ["a","a","c","d","d","d","g","o","o"],
    score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    Output: 23
    Explanation:
    Score  a=1, c=9, d=5, g=3, o=2
    Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
    Words "dad" and "dog" only get a score of 21.

    brute-force...
    Runtime: 48 ms, faster than 85.25% of Python3 online submissions for Maximum Score Words Formed by Letters.

    """

    def solve(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        this version will exceeded the time limit
        """
        letter_quota = Counter(letters)

        # available_candidates
        candidates = [
            LetterCount(i, score)
            for i in words
            if all(j in letter_quota for j in i)
        ]
        return self.get_max_scores(candidates, letter_quota)

    def get_max_scores(self, candidates, letter_quota):
        if not candidates:
            return 0

        result = []
        candidate = candidates[0]

        # select this candidate
        if valid_quota(letter_quota, candidate.letter_count):
            diff = letter_quota - candidate.letter_count
            score = self.get_max_scores(
                candidates[1:], diff
            )
            result.append(candidate.score + score)

        # without this candidate
        result.append(self.get_max_scores(
            candidates[1:], letter_quota
        ))
        return max(result)


def pos_to_char(pos):
    return chr(pos + 97)


class LetterCount:
    def __init__(self, letters, score):
        self.letter_count = Counter(letters)
        self.score = sum(j * score[(ord(i) - 97)] for i, j in self.letter_count.items())


def valid_quota(quota, letter_count):
    keys = quota.keys() | letter_count.keys()
    return all(quota[k] - letter_count[k] >= 0 for k in keys)


class TestMaxScoreWords(unittest.TestCase):
    def test_1(self):
        obj = MaxScoreWords()
        assert (
            obj.solve(
                words=["dog", "cat", "dad", "good"],
                letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                score=[
                    1,
                    0,
                    9,
                    5,
                    0,
                    0,
                    3,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    2,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                ],
            )
            == 23
        )

    def test_2(self):
        obj = MaxScoreWords()
        assert (
            obj.solve(
                words=["xxxz", "ax", "bx", "cx"],
                letters=["z", "a", "b", "c", "x", "x", "x"],
                score=[
                    4,
                    4,
                    4,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    5,
                    0,
                    10,
                ],
            )
            == 27
        )

    def test_3(self):
        obj = MaxScoreWords()
        assert (
            obj.solve(
                words=["leetcode"],
                letters=["l", "e", "t", "c", "o", "d"],
                score=[
                    0,
                    0,
                    1,
                    1,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                ],
            )
            == 0
        )

    def test_4(self):
        obj = MaxScoreWords()
        assert (
            obj.solve(
                words=[
                    "daeagfh",
                    "acchggghfg",
                    "feggd",
                    "fhdch",
                    "dbgadcchfg",
                    "b",
                    "db",
                    "fgchfe",
                    "baaedddc",
                ],
                letters=[
                    "a",
                    "a",
                    "a",
                    "a",
                    "a",
                    "a",
                    "a",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "d",
                    "d",
                    "d",
                    "d",
                    "d",
                    "d",
                    "d",
                    "d",
                    "d",
                    "d",
                    "d",
                    "d",
                    "d",
                    "d",
                    "e",
                    "e",
                    "e",
                    "e",
                    "e",
                    "e",
                    "e",
                    "e",
                    "e",
                    "e",
                    "f",
                    "f",
                    "f",
                    "f",
                    "f",
                    "f",
                    "f",
                    "f",
                    "f",
                    "f",
                    "f",
                    "f",
                    "f",
                    "f",
                    "g",
                    "g",
                    "g",
                    "g",
                    "g",
                    "g",
                    "g",
                    "g",
                    "g",
                    "g",
                    "g",
                    "g",
                    "h",
                    "h",
                    "h",
                    "h",
                    "h",
                    "h",
                    "h",
                    "h",
                    "h",
                    "h",
                    "h",
                    "h",
                    "h",
                ],
                score=[
                    2,
                    1,
                    9,
                    2,
                    10,
                    5,
                    7,
                    8,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                ],
            )
            == 298
        )
