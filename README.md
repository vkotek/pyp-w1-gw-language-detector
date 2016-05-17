# [pyp-w1] Language Detector

You will need to build a program that is able to detect the language of certain piece of text given by the user. For that you will need to respect the following interface:

```python
>>> from .languages import LANGUAGES

>>> user_text = """
Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987), conocido como
Leo Messi, es un futbolista argentino11 que juega como delantero en el Fútbol
Club Barcelona y en la selección argentina, de la que es capitán. Considerado
con frecuencia el mejor jugador del mundo y calificado en el ámbito deportivo
como el más grande de todos los tiempos, Messi es el único futbolista en la
historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de ellos en
forma consecutiva– y el primero en recibir tres Botas de Oro.
Con el Barcelona ha ganado siete títulos de La Liga y cuatro de la Liga de
Campeones de la UEFA, así como tres títulos de la Copa del Rey. Goleador
prolífico, ostenta los récords por más goles en la historia de La Liga (308),
en una temporada de La Liga (50), en un año calendario (91), en un partido de
la Liga de Campeones (cinco) y en más temporadas de la Liga de Campeones (cinco).
"""

>>> detect_language(user_text, LANGUAGES)
'Spanish'
```

Language detection is not magic. It's just a matter of counting how many of the most common words in a language are included in certain text. If given text contains words of different languages, the detector should return the language that contain most words in given text.

You are responsible of defining the set of the most used words in each of the languages you want to support. As a requirement of this group work, we ask you to support at least 3 languages, including: english, spanish and german.

**Get extra credit for +95% code coverage**
