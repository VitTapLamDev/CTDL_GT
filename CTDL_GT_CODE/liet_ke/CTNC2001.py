def generate_binary_sequences(n):
    def generate_sequence(current):
        if len(current) == n:
            print(''.join(current))
            return
        generate_sequence(current + ['0'])
        generate_sequence(current + ['1'])

    generate_sequence([])

n = int(input())
generate_binary_sequences(n)