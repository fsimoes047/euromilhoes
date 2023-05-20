def main():
    chaves =set()
    chave=frozenset()
    cha=set()
    for a in range(1,51):
        for b in range(1,51):
            if b == a:
                continue
            for c in range(1,51):
                if c == a or b==c:
                    continue
                for d in range(1,51):
                    if d==a or d==b or d==c:
                        continue
                    for e in range(1,51):
                        if e==a or e==b or e==c or e==d:
                            continue
                        for ch in [a,b,c,d,e]:
                            cha.add(ch)
                        print(cha)
                        chave=frozenset(cha)
                        cha=set()
                        chaves.add(chave)
                        chave=frozenset()
    print(len(chaves))


if __name__ == '__main__':
    main()