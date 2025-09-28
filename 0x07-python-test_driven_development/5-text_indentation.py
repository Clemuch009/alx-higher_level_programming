#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
       text (str): text to be printed

    >>>  text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit ?Quonam modo?")
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,

    Quonam modo?

    >>> text_indentation(7)
    Teaceback (most recent call last):
        ...
    TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special = ['.', '?', ':']
    for i in text:
        if i not in special:
            print(i, end="")
        else:
            print(i, end="\n\n")
text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
        Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
        Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
        Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
        Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
        rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
        stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
        cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
        beatiorem! Iam ruinas videres""")
