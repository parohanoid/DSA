# Given an array of integers representing the value of cardPoints, write a function to calculate the maximum score you can achieve by selecting exactly k cardPoints from either the beginning or the end of the array.

# For example, if k = 3, then you have the option to select:

# the first three cardPoints,
# the last three cardPoints,
# the first card and the last two cardPoints
# the first two cardPoints and the last card
# Example 1: Input:

cardPoints = [100,40,17,9,73,75]

k = 3
# Output:
# 17

def max_card(cardPoints, k):

    score = sum(cardPoints[:k])
    l_max = sum(cardPoints[-k:])

    max_score = max(score, l_max)

    l = 0
    r = len(cardPoints) - 1
    for i in range(k-1, -1, -1):
        score = score - cardPoints[i] + cardPoints[r]
        max_score = max(max_score, score)
        r -= 1
    return max_score

print(max_card(cardPoints, k))


# their code

def maxScore(cards, k):
  total = sum(cards)
  if k >= len(cards):
    return total

  state = 0
  max_points = 0
  start = 0

  for end in range(len(cards)):
    state += cards[end]

    if end - start + 1 == len(cards) - k:
      max_points = max(total - state, max_points)
      state -= cards[start]
      start += 1

  return max_points