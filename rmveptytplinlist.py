a=[12,34,(),345,(),435]
for i in a:
    if (i==()):
        a.remove(i)
print(a)