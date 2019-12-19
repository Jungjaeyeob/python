def gugudan ( data ):
    for dan in data :
        for num in range(1,10):
            dab = dan * num
            print('%d * %d = %d' % (dan, num, dab))

while True:
    print('''1.홀수단 출력
2. 짝수단 출력
3. 전체단 출력
4. 특정단 출력
5. 종료''')
    menu = input()

    start = 2
    end = 10
    step = 1
    
    if menu == '1':
        start = 3
        step  = 2
    elif menu == '2':
        start =2
        step = 2
    elif menu == '3':
        pass
    elif menu == '4':
        start = input('특정 단을 입력')
        end = start + 1


    data = range(start, end, step)
    gugudan(data)
