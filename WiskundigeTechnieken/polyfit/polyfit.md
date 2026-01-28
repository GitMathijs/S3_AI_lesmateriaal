# Onderzoek numpy.polyfit

Door: Mathijs de Jong

## Inleiding

De functie polyfit is onderdeel van de numpy library. Het is een veel gebruikte functie die het mogelijk maakt om een polynoom op datapunten te fitten. Zo wordt de functie bijvoorbeeld gebruikt om trendlijnen te berekenen voor data in grafieken, zowel lineair, kwadratisch als met hogere-orde polynomen. Binnen de functie wordt de least squares methode gebruikt om te bepalen hoe goed de polynoom op de datapunten fit (NumPy Developers, z.d.).

Tijdens het project in samenwerking met de fysio studenten en FC Utrecht, heeft mijn groep gebruikt gemaakt van deze functie. Zo hebben we een lineaire trendlijn gefit op datapunten om een Load-Velocity Profile (LVP) te maken. Daarnaast hebben we ook een parabolische trendlijn gefit op datapunten om een Load-Power Profile te maken (LPP). 

## Werking

De wiskundige notitie van een polynoom is als volgt:

$p(x) = p_0 + p_1x + p_2x^2 + ... + p_nx^n$

Polyfit vindt de best passende polynoom (van de opgegeven graad) voor de gegeven datapunten d.m.v. de least squares methode. Dat wil zeggen dat polyfit waarden vindt voor de coëfficiënten $p_0$, $p_1$, $p_2$ etc. zodat de som van de kwadraten van de afwijkingen tussen p(x) en de y-waarden minimaal is. Om deze coëfficiënten te vinden, lost de functie intern een Vandermonde-matrix op (NumPy Developers, z.d.). Dit is een matrix met de voorwaarde dat elke rij in de matrix uit een meetkundige rij moet bestaan, oftewel een $m$ x $n$ matrix in deze vorm (Vandermonde-matrix, z.d.): 

![Vandermonde-matrix voorbeeld](vandermonde-matrix.svg)

### Parameters

De functie heeft 3 verplichte parameters, en 4 optionele. Ik leg voor elke parameter kort uit wat deze betekent:

__x__: de x-coördinaten van de data waarop je de polynoom wilt fitten.  
__y__: de y-coördinaten van de data waarop je de polynoom wilt fitten.  
__deg__: graad van de polynoom die je wilt fitten. Als je kiest voor 1, dan is dat lineaire regressie. Als je kiest voor 2, dan is dat kwadratische regressie (voor een parabool). De maximale graad die je kunt gebruiken is in principe het aantal punten minus 1, maar een hoge graad zorgt wel voor problemen zoals numerieke instabiliteit. De documentatie raadt aan om numpy.polynomial.polynomial.polyfit te gebruiken bij hogere orde fits.  
__rcond__: optioneel, bepaalt welke kleine getallen genegeerd moeten worden bij het oplossen van de matrix.  
__full__: optionele boolean, geeft extra diagnostische informatie terug, zoals de foutresidu en matrixrang. Staat standaard op False.  
__w__: optioneel, een array met gewichten voor de datapunten. Dit is handig als sommige punten zwaarder mee moeten wegen, omdat ze bijvoorbeeld betrouwbaarder zijn.  
__cov__: optionele boolean, geeft ook de covariantiematrix van de coëfficiënten terug. Staat standaard op False.

### Returns

De return-waarde is standaard een array met de coëfficiënten van de best fittende polynoom. De volgorde is van hoogste macht naar laagste macht.

Wanneer de parameters full en cov op True staan, wordt er naast de coëfficiënten extra informatie meegegeven, zoals bijvoorbeeld de covariantie matrix.

## Gebruikte bronnen

NumPy Developers. (z.d.). *numpy.polyfit*. NumPy Documentation. Geraadpleegd op 28 januari 2026, van https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html

Vandermonde-matrix. (z.d.). *Wikipedia: de vrije encyclopedie*. Geraadpleegd op 28 januari 2026, van https://nl.wikipedia.org/wiki/Vandermonde-matrix