def generate_binaries(n, current_combination, index):
  if index == n:
    print("".join(str(x) for x in current_combination))
  else:
    current_combination[index] = 0
    generate_binaries(n, current_combination, index + 1)
    current_combination[index] = 1
    generate_binaries(n, current_combination, index + 1)

n = int(input())
generate_binaries(n, [0] * n, 0)