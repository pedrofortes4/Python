# SETS
c = {1, 2, 3, 4, 4, 2}          # Sets não repetem seus elementos, e sempre os mostram ordenados. c = {1, 2, 3, 4}
print(type(c))
c.add(5)
print(c)
d = set()
d.add(7)
d.add(6)
print(d)
b = c.union(d)      # União de dois conjuntos, retirando repetições
print(b)
b.add('v')          # Adicionar elemento ao conjunto
print(b)
b.discard('v')      # Descartar elemento do conjunto
print(b)
f = {1, 3, 4, 6, 7, 9}
g = {0, 1, 2, 3, 6, 7, 10}
print('F:', f)
print('G:', g)
print('F U G:', f.union(g))
print('F interseção G:', f.intersection(g))        # Interseção entre f e g
print('F - G:', f.difference(g))                   # Diferença de conjuntos
print('G - F:', g.difference(f))
print('Diferença simétrica F e G:', f.symmetric_difference(g))      # Dif. Sim. F:G - Conjunto dos elementos exclusivos de cada grupo
print('Diferença simétrica G e F:', g.symmetric_difference(f))
print(f.issubset(g))            # Verificar se F é subconjunto de G (False)
h = {0, 1, 2, 3, 4}
i = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(h.issubset(i))            # True
print(h.issuperset(i))            # False
print(i.issuperset(h))            # True
