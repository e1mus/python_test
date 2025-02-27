friends = {"Bob" , "Rolf" , "Anne"}
abroad = {"Bob" ,  "Anne"}

local_friends = friends.difference(abroad)


local = { "Rolf" }


friends = local.union(abroad)
print(friends)

