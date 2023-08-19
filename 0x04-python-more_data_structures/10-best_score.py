#!/usr/bin/python3


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    mk = list(a_dictionary.keys())[0]
    mx = a_dictionary[mk]
    for k, v in a_dictionary.items():
        if mx < v:
            mx = v
            mk = k
    return (mk)
