def main():
    f=open('result.txt', 'w')
#    f.write('chaves=[')
    chaves =[]
    chave=frozenset()
    cha=set()
    for a in range(1,51):
        print(a)
        for b in range(1,51):
            for c in range(1,51):
                for d in range(1,51):
                    for e in range(1,51):
                        cha = set([a,b,c,d,e])
                        if len(cha) < 5:
                            cha=set()
                        else:
                            for i,j in enumerate(cha):
                                if i<4:
                                    f.write(str(j)+',')
                                else:
                                    f.write(str(j)+';')




#    f.write(']')
    f.close()


if __name__ == '__main__':
    main()