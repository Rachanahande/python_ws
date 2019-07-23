'''1.	Writeaprogramtogenerateafancynumberforanewvehicleconsideringthefollowingconstraints:
a.	Thefancynumbershouldhave4-digits.
b.	Thesumofthese4-digitsshouldbe12.
c.	The3rddigitshouldbeequaltothedifferencebetweenthe1standthe2nddigit.
d.	The4thdigitshouldbeequaltothesumofthe1standthe3rddigit.

Theprogramshouldbeabletogenerateallthepossible4-digitnumbersthatmeettheabovelistedcriteria.'''

def get_digits(num):
    temp = num
    a,temp = temp // 1000, temp % 1000
    b,temp = temp // 100, temp % 100
    c,temp = temp // 10, temp % 10
    d,temp = temp // 1, temp % 1
for i in range (1000,10000):
    if sum_digits(i) == 12:
        a,b,c,d = get_digits(i)
        if a-b == c and a+c