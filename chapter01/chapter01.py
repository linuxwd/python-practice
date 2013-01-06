movies=["The Holy Grail","The Life of Brian","The Meaning of Life"]
print(movies)

for i in movies:
    print(i)

print("##############################")
print(movies[1])
print(movies[0])
print(movies[2])
print("##############################")
cast=["Cleese","Palin","Jones","Idle"]
print(cast)
print(len(cast))
print(cast[1])
cast.append("Gilliam")
print(cast)
print(cast.pop())
print(cast)
cast.extend(["Gilliam","Chapman"])
print(cast)
print(cast.remove("Chapman"))
print(cast)
cast.insert(0,"Chapman")
print(cast)
print(movies)
movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983)
print (movies)
movies=["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]
print(movies)

fav_movies=["The Holy Grail","The Life of Brian"]
print(fav_movies[0])
print(fav_movies[1])

print("##############################")
for each_flick in fav_movies:
    print(each_flick)
count=0
for i in range(1,100):
    count+=i

print(count)

count=0
while count<len(movies):
    print(movies[count])
    count+=1

print(count)
movies=["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Plain","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
print(movies)
print(movies[4][1][3])
for each_item in movies:
    print(each_item)
names=["Michael","Terry"]
print (isinstance(names,list))
num_names=len(names)
print(isinstance(num_names,list))
print("##############################")
for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)


print("##############################")
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
           print_lol(each_item)
        else:
            print(each_item)
print_lol(movies)


































































































