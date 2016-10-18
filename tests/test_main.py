# -*- coding: utf-8 -*-
import unittest

from language_detector import detect_language
from language_detector.languages import LANGUAGES


class TestLanguageDetector(unittest.TestCase):

    def test_detect_language_spanish(self):
        text = """
            Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
            conocido como Leo Messi, es un futbolista argentino11 que juega
            como delantero en el Fútbol Club Barcelona y en la selección
            argentina, de la que es capitán. Considerado con frecuencia el
            mejor jugador del mundo y calificado en el ámbito deportivo como el
            más grande de todos los tiempos, Messi es el único futbolista en la
            historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
            ellos en forma consecutiva– y el primero en
            recibir tres Botas de Oro.
        """
        result = detect_language(text, LANGUAGES)
        self.assertEqual(result, 'Spanish')

    def test_detect_language_german(self):
        text = """
            Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
            Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
            der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
            erzielte. Inzwischen hat Messi als einziger Spieler mehr als 300
            Erstligatore erzielt und ist damit Rekordtorschütze
            der Primera División.
        """
        result = detect_language(text, LANGUAGES)
        self.assertEqual(result, 'German')

    def test_detect_language_mixed_languages(self):
        text = """
            # spanish
            Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
            conocido como Leo Messi, es un futbolista argentino11 que juega
            como delantero en el Fútbol Club Barcelona y en la selección
            argentina, de la que es capitán.

            # german
            Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
            Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
            der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
            erzielte.
        """
        result = detect_language(text, LANGUAGES)
        self.assertEqual(result, 'Spanish')

    def test_detect_language_english(self):
        # NOTE: You will first need to define a new "English" language
        #       in the languages.py module.
        text = """
            # english
            Lionel Andrés 'Leo' Messi is an Argentine professional footballer
            who plays as a forward for Spanish club FC Barcelona and the
            Argentina national team. Often considered the best player in the
            world and rated by many in the sport as the greatest of all time,
            Messi is the only football player in history to win five FIFA
            Ballons, four of which he won consecutively, and the first player
            to win three European Golden Shoes.
        """
        result = detect_language(text, LANGUAGES)
        self.assertEqual(result, 'English')
