import notwordle

def test_get_random_word():
    """Tests that a random word from the word list is chosen."""
    word_list = ['SNAKE', 'CRANE', 'WYRDL']
    assert notwordle.get_random_word(word_list) in word_list

