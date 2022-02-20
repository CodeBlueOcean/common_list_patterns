basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print(basket[::-1])
## print(basket[::-1]) means reverse, but balance out with basket.reverse() 
print(basket)

print(list(range(101)))

#''.join()

sentence = '!'
new_sentence = sentence.join(['hi','my','name','is','JOJO'])
print(new_sentence)


sentence = ' '
new_sentence = sentence.join(['hi','my','name','is','JOJO'])
print(new_sentence)

# another way to do this below
new_sentence = ' '.join(['hi','my','name','is','JOJO'])
print(new_sentence)

