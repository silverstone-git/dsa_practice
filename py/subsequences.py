def print_subsequences(seq):
    def recursive_print(seq, index, current_subsequence):
        if index == len(seq):
            print(current_subsequence)
            return
        recursive_print(seq, index + 1, current_subsequence)
        recursive_print(seq, index + 1, current_subsequence + seq[index])

    recursive_print(seq, 0, "")

# Example usage:
seq = "abcd"
print_subsequences(seq)
