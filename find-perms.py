#!/usr/bin/env python3


# Finds all permutations of s iteratively. As expected, this is quite slow.
# Also, the algorithm's performance is hit badly if s contains repeated chars.
def find_perms(s):
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


if __name__ == '__main__':
    english_dict = set(['day', 'hello', 'raw', 'war', 'world'])

    for scrambled_word in ['ehlol', 'arw', 'lordw', 'xyz']:
        perms = find_perms(list(scrambled_word))
        matches = perms & english_dict

        if matches:
            print(f'found {len(matches)} permutation(s) of '
                  f'\'{scrambled_word}\' in the dictionary: ', end='')

            print(', '.join(list(matches)), end='.\n')
        else:
            print(f'no permutation of \'{scrambled_word}\' was found in the '
                  f'dictionary.')
