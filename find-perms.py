#!/usr/bin/env python3


# Finds all permutations of s iteratively. As expected, this is quite slow.
# Also, the algorithm's performance is hit badly if s contains repeated chars.
def find_perms_iterative(s):
    n, perms = len(s), set()

    for fixed in range(n):  # Outer loop.

        # Fix a different char. every time.
        s[0], s[fixed] = s[fixed], s[0]

        for _ in range(n - 1):  # Middle loop.

            for i in range(1, n - 1):  # Inner loop.

                # Swap the i-th letter with the (i + 1)-th.
                s[i], s[i + 1] = s[i + 1], s[i]

                perm = ''.join(s)

                if perm not in perms:
                    perms.add(perm)

    return perms


# Simple recursive scheme for finding all permutations of s. Just as the
# iterative version, this returns a set with all permutations. Same caveats
# also for strings with repeated characters.
def find_perms_recursive(s):
    def find_perms_recursive_helper(s, left, right):
        if (left == right):
            perm = ''.join(s)

            if perm not in perms:
                perms.add(perm)

            return

        for i in range(left, right + 1):
            s[i], s[left] = s[left], s[i]
            find_perms_recursive_helper(s, left + 1, right)
            s[i], s[left] = s[left], s[i]

    perms = set()

    # Fill the set of permutations.
    find_perms_recursive_helper(s, 0, len(s) - 1)

    return perms


if __name__ == '__main__':
    english_dict = set(['day', 'hello', 'raw', 'war', 'world'])

    for scrambled_word in ['ehlol', 'arw', 'lordw', 'xyz']:
        perms = find_perms_recursive(list(scrambled_word))
        matches = perms & english_dict

        if matches:
            print(f'found {len(matches)} permutation(s) of '
                  f'\'{scrambled_word}\' in the dictionary: ', end='')

            print(', '.join(list(matches)), end='.\n')
        else:
            print(f'no permutation of \'{scrambled_word}\' was found in the '
                  f'dictionary.')
