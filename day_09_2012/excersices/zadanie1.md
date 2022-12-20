Wykonaj funkcję z ```precondition``` i ```postcondition```
Niech funkcja ```precondition``` ma trzy parametry wejściowe ```miesięczna wpłata ubezpieczenia, procent premii miesięcznej, początkowa data wpłaty```. 

Funkcja powinna liczyć, ile kapitału uzbiera ubezpieczona osoba w takim czasie (do ostatniego pełnego miesiąca)
wg daty systemowej w komputerze.
```
np. dla 5 miesięcy i składki 100 zł i 5%
1 miesiąc = 100 + 5 = 105
2 miesiąc + 100 = 205 + 10,25 = 215.25
3 miesiąc + 100 = 315.25 + 15,7625 = 331.01
...
```

w ```postcondition``` trzeba sprawdzić, czy ```wartość końcowa jest większa niż (miesięczna składka * ilość miesięcy) * procent```
oraz czy zwracana wartość jest typu ```float```