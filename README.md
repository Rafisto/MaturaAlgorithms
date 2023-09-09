# Matura Algorithms

A collection of algorithms written in python,
which are required by the irrelevant Polish IT curriculum.
Yet to ideally pass the exam well above the desired score,
one should at least know their existence.

Clone the repository with:

```bash
git clone https://github.com/Rafisto/MaturaAlgorithms.git
```

## Algorithms

1. [Primality test - Czy liczba jest liczbą pierwszą?](python/checkPrime.py)
2. [Base converter - Zamiana systemów liczbowych, na (10) oraz (dowolny) z (10)](python/convertSystems.py)
3. [LCM, GCD Calculator - Liczenie NWW oraz NWD](python/GCDLCM.py)
4. [Text comparison - Porównywanie tekstów](python/compareText.py)
5. [Naive pattern matching - Wyszukiwania Wzorca (WW) metodą naiwną](python/naivePatternSearching.py)
6. [Caesar cipher - Szyfr przestawieniowy Cezara (ROT13), w ogólności ROT(n)](python/rotEnc.py)
7. [Insertion Sort - Metoda sortowania poprzez wstawianie](python/instertionSort.py)
8. [Bubble Sort - Metoda sortowania bąbelkowego](python/bubbleSort.py)
9. [Iterative progression - Liczenie wyrazów ciągu metodą iteracyjną](python/iterativeProgression.py)
10. [Recursive progression - Liczenie wyrazów ciągu metodą rekurencyjną](python/recursiveProgression.py)
11. [Fibonacci sequence - Liczenie wyrazów ciągu Fibonacciego](python/fibonacci.py)
12. [Bisection method - Wyszukiwanie pierwiastków wielomianu metodą połowienia](python/bisection.py)
13. [Euclidean algorithm - algorytm Euklidesa w wersji iteracyjnej i rekurencyjnej](python/euclideanAlgorithm.py)
14. [Binary search - wyszukiwanie binarne](python/binarySearch.py)
15. [Eratosthenes sieve - generowanie liczb pierwszych z użyciem sita Eratostenesa](python/eratosthenesSieve.py)
16. [Merge sort - sortowanie ciągu poprzez scalanie](python/mergeSort.py)
17. [Babylonian method - wyszukiwanie pierwiastków kwadratowych metodą babilońską](python/babylonianMethod.py)
18. [Horner's method - wartości wielomianu schematem Hornera](python/hornerPolynomialEvaluation.py)
19. [Exponentiation by squaring - szybkie potęgowanie liczb w wersji iteracyjnej i rekurencyjnej](python/squaringExponentiation.py)
20. [Prime factorization - rozkładanie liczby na czynniki pierwsze](python/primeFactorization.py)
21. [Progression properties - najdłuższy spójny podciąg niemalejący, spójny podciąg o największej sumie](python/longestNonDecreasing.py) 
22. [Postfix notation - implementacja kalkulatora przy użyciu odwróconej notacji polskiej](python/postfixNotation.py)

## Polish Description

[Source (cke.gov.pl)](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Informatory/2023/Aneks_2023_2024_informatyka_EM_F23.pdf)
<br/>

#### Poziom podstawowy. Zdający:

1) planuje kolejne kroki rozwiązywania problemu, z uwzględnieniem podstawowych
   etapów myślenia komputacyjnego (określenie problemu, definicja modeli i pojęć,
   znalezienie rozwiązania, zaprogramowanie i testowanie rozwiązania).
2) stosuje przy rozwiązywaniu problemów z różnych dziedzin algorytmy poznane
   w szkole podstawowej oraz algorytmy:
    - a) na liczbach: badania pierwszości liczby
    - zamiany reprezentacji liczb między pozycyjnymi systemami liczbowymi,
    - działań na ułamkach z wykorzystaniem NWD i NWW,
    - b) na tekstach: porównywania tekstów,
    - wyszukiwania wzorca w tekście metodą naiwną,
    - szyfrowania tekstu metodą Cezara i przestawieniową,
    - c) porządkowania ciągu liczb: przez wstawianie
    - oraz metodą bąbelkową,
    - d) obliczania wartości elementów ciągu metodą iteracyjną i rekurencyjną,
    - ^^w tym wartości elementów ciągu Fibonacciego.

3) wyróżnia w problemie podproblemy i charakteryzuje:
    - metodę połowienia
    - stosuje podejście zachłanne i rekurencję;

#### Poziom rozszerzony. Zdający:

1) zapisuje za pomocą listy kroków, schematu blokowego lub pseudokodu,
   i implementuje w wybranym języku programowania, algorytmy poznane na
   wcześniejszych etapach oraz algorytmy:
    - a) algorytm Euklidesa w wersji iteracyjnej i rekurencyjnej wraz
      z zastosowaniami,
    - b) znajdowania określonego elementu w zbiorze: elementu w zbiorze
      uporządkowanym metodą binarnego wyszukiwania,
    - c) generowania liczb pierwszych metodą sita Eratostenesa,
    - d) sortowania ciągu liczb przez scalanie,
    - e) wyznaczania miejsc zerowych funkcji metodą połowienia,
    - f) obliczania przybliżonej wartości pierwiastka kwadratowego,
    - g) obliczania wartości wielomianu za pomocą schematu Hornera,
    - h) szybkiego potęgowania liczb w wersji iteracyjnej i rekurencyjnej,

2) wykorzystuje znane sobie algorytmy przy rozwiązywaniu i programowaniu
   rozwiązań następujących problemów:

    - a) rozkładania liczby na czynniki pierwsze,
    - b) wykonywania działań na liczbach w systemach innych niż dziesiętny,
    - c) znajdowania w ciągu podciągów o różnorodnych własnościach, np.
      najdłuższego spójnego podciągu niemalejącego, spójnego podciągu o największej sumie,
    - d) zamiany wyrażenia na postać w odwrotnej notacji polskiej i obliczanie jego
      wartości na podstawie tej postaci,

3) objaśnia, a także porównuje podstawowe metody i techniki algorytmiczne oraz
   struktury danych, wykorzystując przy tym przykłady problemów i algorytmów,
   w szczególności:
    - a) wyszukiwanie elementów liniowe i przez połowienie (do znajdowania
      elementów w zbiorze, sortowania przez wstawianie, przybliżonego
      rozwiązywania równań),
    - b) rekurencję (do generowania ciągów liczb, potęgowania, sortowania liczb,
      generowania fraktali),
    - c) metodę dziel i zwyciężaj (sortowanie przez scalanie i szybkie),
    - d) podejście zachłanne,
    - e) programowanie dynamiczne,
    - f) struktury dynamiczne: stos, kolejka, lista (do realizacji algorytmu ONP)

# Matura Results

![Matura Results](/results/PLOT.png)

#### Personal opinion on the results

As clearly visible on the plot, basic exams - polish, mathematics and english are specifically fixed to enable the highest number of students to pass.
Polish and english on a basic level was failed by no more than 5% of the students and basic mathematics less than 15%. Congratulations to all who received a reasonable score.<br/>

My score on the advanced mathematics: 100%<br/>
My score on the advanced physics: 78%<br/>
My score on the advanced informatics: 78%<br/>

Notably won an olympiad.

# Last Year [2022-2023] Comparison

![Matura Comparison](/results/PLOT-COMPARISON.png)

#### Personal opition on the comparison

In 2023 Matura was a little (up to 10%) easier than a year prior.
