
# sum = 0
# for i in range(300, 2100):
#     if i % 7 == 0 and i % 13 != 0:
#         print i
#         sum += i
#     elif i % 13 == 0 and i % 7 != 0:
#         print i
#         sum += i
# print sum


# sum = 0
# for i in range(300, 2101):
#     if i % 7 == 0 or i % 13 == 0:
#         print i % 7, i % 13
#         sum += i
# print sum

# Fibonacci

# def F(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return F(n-1)+F(n-2)

# def f(n):
#     a, b = 0, 1
#     for i in range(0, n):
#         a, b = b, a + b
#     return a 

# i = 10000000
# while True:
#     out = f(i)
#     print out
#     if len(str(out)) == 11:
#         print i
#         import sys
#         sys.exit()
#     i = i + 1

# String
# def how_many(inp):
#     letters = []
#     for i in range(len(inp)):
#         t = inp[i]
#         if t not in letters:
#             letters.append(t)
#     # print letters
#     return len(letters)


# inp = 'effnbebmcakjbekamecdddgjmhemaminjjlifeidcnfhmgdhmcldlidhjbiacdmdaajkedegdnhimfckkhijblnklgkjhlmfeickbicnhdmdmdhikkckbbdnjkbegggbmmhnkmkghignnkkiajmhjidlekkdkceiifibbmmaaecmcldngbgmmkfbhaigbikehjaeaffgfimgmkhhnjbcccgggbnadbadgdhhiccahgenlhlgdamfndcamjhlgffhhadihbkekdammgllgmnamkliaanlmcajielfhdgihclmmfacghdajgfdfglbfnhnaickiflilkhblcdfhfcgideeebfccnnhibadiblbegcefgmeflkbbgkbhdnijfgcjnkmaamggebajcfalcfklbidkejfhghlageemgamjhialgecghjimeihlfnlgjckeafigfjafkfalnndnfihdjkidmilfheifgkejnaagkklkfdanhllmibhmebbedcngcnkmfcdbhjlnhaciengildldljccfneagccbdbljgfamlfkhcdjmddagkggmejmhdcianlackmdffjkjnchklfchaahfmenccghaglglhchjdaabfafcgnjmgkfnhndnbakkaimacdcggehiggdiflajgnfcnkanggiddnincaegffiackfffknijnmmggcbkmjmigkefjkhhcdfdfbbfnmmifdbkeieibhhiaakikgcfjficbmbiefkeahlbanglkicjaiihkklaccchfcmakmmchdabkgbflffngfaeaacbfdagnjbleieegchmnmeafhnhjgmhnjffhfbclgmclhahihhjjfihfhclkgkkdkkafflanfjendnfnlhffjajkdmlihklfmnaejlnhglcbdclbdkgljddcnhjkjhalkjnlbcddgfalklddjeblldihhlclkkbmembkgdnlmlcnijbcmlfgcifgbkfae'

# str_len = len(inp)
# highest = 0
# keys = ''

# for i in range(str_len+1):
#     for j in range(str_len+1):
#         test = inp[j:i]
#         if how_many(test) == 3 and len(test) > highest:
#             print keys
#             highest = len(test)
#             keys = test
# print keys

# Arithmetic
import urllib2
# response = urllib2.urlopen('http://url-riddle.herokuapp.com/riddles/shipyard/bigleague/challenge')
# html = response.read()
# alls = html.split(" ")
# first = int(alls[0])
# second = int(alls[-1])

# res = first*second
# resp_url = 'http://url-riddle.herokuapp.com/riddles/shipyard/bigleague/%i' % res

# response = urllib2.urlopen(resp_url)
# print response.read()


# Primes
# def is_prime(n):
#     for i in range(3, n):
#         if n % i == 0:
#             return False
#     return True

# response = urllib2.urlopen('http://url-riddle.herokuapp.com/riddles/shipyard/primes/challenge')
# first = int(response.read())
# print first
# first += 1
# while True:
#     print first
#     if not is_prime(first):
#         first += 1
#     else:
#         print first
#         break

# resp_url = 'http://url-riddle.herokuapp.com/riddles/shipyard/primes/%i' % first
# response = urllib2.urlopen(resp_url)
# print response.read()

# Coordinates
from Goulib import homcoord
start = homcoord.Pt(23, 15)

fm = homcoord.Xlate(2, -6)
first = fm.apply(start)

sm = homcoord.Xscale(1, 3, 0.5)
second = fm.apply(first)

print second
second = homcoord.Pt(13, 4)

tm = homcoord.Xrotaround(homcoord.Pt(3,2), 1.57079632679)
third = tm.apply(second)

print 'third', third

# manual mirror
# fourth = homcoord.Pt(2,-26)
fourth = homcoord.Pt(2,-12)
print 'fourth', fourth

fifthm = homcoord.Xlate(3, -2)
fifth = fm.apply(fourth)
print 'fifth', fifth

fifth = homcoord.Pt(5, -14)

sixm = homcoord.Xscale(-8, 0, 4.5)
sixth = fm.apply(fifth)

sevm = homcoord.Xrotaround(homcoord.Pt(1,-3), 3.14159265359)
seven = tm.apply(sixth)


print 'seven', seven

