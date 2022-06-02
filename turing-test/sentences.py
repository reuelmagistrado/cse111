# import random module
import random


def main():
    # Singular Noun in Past Tense
    single_past = f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, 'past')} {get_prepositional_phrase(1)}."

    # Singular Noun in Present Tense
    single_present = f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, 'present')} {get_prepositional_phrase(1)}."

    # Singular Noun in Future Tense
    single_future = f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, 'future')} {get_prepositional_phrase(1)}."

    # Plural Noun in Past Tense
    plural_past = f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, 'past')} {get_prepositional_phrase(2)}."

    # Plural Noun in Present Tense
    plural_present = f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, 'present')} {get_prepositional_phrase(2)}."

    # Plural Noun in Future Tense
    plural_future = f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, 'future')} {get_prepositional_phrase(2)}."

    print(single_past)
    print(single_present)
    print(single_future)
    print(plural_past)
    print(plural_present)
    print(plural_future)


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                     "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think",
                     "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

    verb = random.choice(verbs)
    return verb


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    preposition = random.choice(prepositions)
    return preposition


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """

    prepositional_phrase = f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"
    return prepositional_phrase


def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
        "ancient", "combative", "cute", "dangeorus", "graceful", "handsome", "lazy", "massive", "miniscule", "petite", "puny", "ugly", "wild"

    Return: a randomly chosen adjective.
    """

    adjectives = ["ancient", "combative", "cute", "dangeorus", "graceful",
                  "handsome", "lazy", "massive", "miniscule", "petite", "puny", "ugly", "wild"]

    adjective = random.choice(adjectives)
    return adjective


# run the main() if it run directly not imported
if __name__ == "__main__":
    main()
