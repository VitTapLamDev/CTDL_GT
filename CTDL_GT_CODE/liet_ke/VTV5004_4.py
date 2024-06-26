def generate_permutations(arr):
    def backtrack(current_permutation, used):
        if len(current_permutation) == len(arr):
            print(' '.join(map(str, current_permutation)))
            return
        for i in range(len(arr)):
            if not used[i]:
                used[i] = True
                current_permutation.append(arr[i])
                backtrack(current_permutation, used)
                current_permutation.pop()
                used[i] = False

    arr.sort()
    used = [False] * len(arr)
    backtrack([], used)

n = int(input())
arr = list(map(int, input().split()))

generate_permutations(arr)
