Lista_zakupów = {'piekarnia':['chleb','bułki','pączek'],'warzywniak':['marchew','seler','rukola']}
counter = 0
print('Lista zakupów')
for shop, products  in Lista_zakupów.items():
   print('Idę do %s, kupuję tu następujące rzeczy: %s.' % (shop.upper(), ", ".join(products).upper()))
   counter += len(products)
print('W sumię kupuję %d produktów.' % counter)