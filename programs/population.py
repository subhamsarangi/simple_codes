def nb_year(p0, percent, aug, p):
    n=0
    p1=p0
    while p0<p:
        n=n+1
        p0+=p0*(percent/100) + aug
    print('It takes',n,'years to reach ',p,' from ',p1,' with ',percent,' percent growth rate and ',aug,' people from outside per year')
   
nb_year(1500, 5, 100, 5000)
nb_year(1500000, 2.5, 10000, 2000000)
nb_year(1500000, 0.25, 1000, 2000000)