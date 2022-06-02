from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():

    # 1. Test singular nouns
    single_noun = ["bird", "boy", "car", "cat", "child",
                   "dog", "girl", "man", "rabbit", "woman"]
    # loop the length of single noun list
    for _ in range(len(single_noun)):
        word = get_noun(1)
        assert word in single_noun

    # 2. Test plural nouns
    plural_noun = ["birds", "boys", "cars", "cats", "children",
                   "dogs", "girls", "men", "rabbits", "women"]

    # loop the length of plural noun list
    for _ in range(len(plural_noun)):
        word = get_noun(2)
        assert word in plural_noun


def test_get_verb():

    # 1. Test the past tense verbs
    past_verb = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(len(past_verb)):
        word = get_verb(1, 'past')
        assert word in past_verb

    # 2. Test the singular present tense verbs
    single_present = ["drinks", "eats", "grows", "laughs", "thinks",
                      "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(12):
        word = get_verb(1, 'present')
        assert word in single_present

    # 3. Test the plural present tense verbs
    plural_present = ["drink", "eat", "grow", "laugh", "think",
                      "run", "sleep", "talk", "walk", "write"]

    for _ in range(12):
        word = get_verb(2, 'present')
        assert word in plural_present

    # 4. Test the future tense verbs
    future_verb = ["will drink", "will eat", "will grow", "will laugh",
                   "will think", "will run", "will sleep", "will talk",
                   "will walk", "will write"]

    for _ in range(12):
        word = get_verb(1, 'future')
        assert word in future_verb


def test_get_preposition():

    # Test the get_preposition() if it is in prepositions list
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    for _ in range(len(prepositions)):
        word = get_preposition()
        assert word in prepositions


def test_get_prepositional_phrase():

    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    # 1. Test singular prepositional phrase
    single_determiner = ["a", "one", "the"]
    single_noun = ["bird", "boy", "car", "cat", "child",
                   "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(4):
        word = get_prepositional_phrase(1).split()
        assert len(word) == 3
        assert word[0] in prepositions
        assert word[1] in single_determiner
        assert word[2] in single_noun

    # 2. Test plural prepositional phrase
    plural_determiner = ["two", "some", "many", "the"]
    plural_noun = ["birds", "boys", "cars", "cats", "children",
                   "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(4):
        word = get_prepositional_phrase(2).split()
        assert len(word) == 3
        assert word[0] in prepositions
        assert word[1] in plural_determiner
        assert word[2] in plural_noun


def test_get_adjective():
    # Test get_adjectives() if it is in adjectives list
    adjectives = ["ancient", "combative", "cute", "dangeorus", "graceful",
                  "handsome", "lazy", "massive", "miniscule", "petite", "puny", "ugly", "wild"]

    for _ in range(len(adjectives)):
        word = get_adjective()
        assert word in adjectives


    # Call the main function that is part of pytest so that the
    # computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
