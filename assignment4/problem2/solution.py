# The elaborate thought process behind this code is explained in our groups' Writing Assignment 4, Problem 2.

def LPS (A, B):
  LPS_DP = [[0]*(len(B)+1) for i in range(len(A)+1)]

  for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
      if(A[i-1] == B[j-1]):
        LPS_DP [i][j] = 1 + LPS_DP[i-1][j-1]

      else:
        LPS_DP [i][j] = max(LPS_DP [i-1][j], LPS_DP [i][j-1])

  print(LPS_DP[(len(A))][len(B)])

line_1 = input()

# Longest palindromic subsequence is the longest common subsequence between string A and reverse of string A
LPS(line_1, line_1[::-1])
