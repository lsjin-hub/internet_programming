for row in range(1,10):
    for col in range(1,10):
        print("{} x {} = {}".format(row,col,row*col))
    print("\n")

    # "{} x {} = {}" -> 문자열인데 {}안에 넣을걸
    # .format(row,col,row*col)

    #row 행 가로/ col 열 세로