#문제 3-1
naver_closing_price=[474500,461500,501000,500500,488500]
print("종가:",naver_closing_price)

#문제 3-2
print("가장 높았던 가격:",max(naver_closing_price))

#문제 3-3
print("가장 낮았던 가격:",min(naver_closing_price))

#문제 3-4
print("가장 높았던 요일과 낮았던 요일의 가격 차:",max(naver_closing_price)
    -min(naver_closing_price))

#문제 3-5
print("수요일의 종가:",naver_closing_price[2])

#문제 3-6
naver_closing_price2={ "09/07":474500, "09/08":461500, "09/09":50100,
    "09/10":500500, "09/11":488500}
print(naver_closing_price2)

#문제 3-7
print("09/09일의 종가:",naver_closing_price2["09/09"])
