print "You are now in a dark forest with two paths. You have to choose the path #1 , #2 or path #3"
path = raw_input("> ")
if path == "1":
    print "There's a man without a face standing near tree and looking at you. What do you do?"
    print "1. attack him."
    print "2. hiding behind a tree."
    man_without_a_face = raw_input("> ") 
    if man_without_a_face == "1":
        print "The man without a face falls to the ground, and you're running away from him."
    elif man_without_a_face == "2":
        print "The man without a face finds you for tree and pulls out his heart.  Good job!"
    else:
        print "Just look at you for five minutes and leave the forest."
elif path == "2":
    print "You see a small house and a path forward."
    print "1. broke the door."
    print "2. Knock on the door."	
    print "3. Go down the path."
    door = raw_input("> ")
    if door == "1":
        print "The dogs eats your legs off."
    elif door == "2":
        print "Door open granny, she will feed you, then you will eat."
    elif door == "3":
        print "You walk a hundred meters and you find the highway. Congratulations! You left the forest."    
elif path == "3":
    print "You are very hangry. You see the bushes with berries, there are two kinds of red and blue berries. What do you eat?"
    print "1. eat red berry"
    print "2. eat blue berry"
    berry == raw_input("> ")
    if berry == "1":
        print "You start to fail, and you went to fight with a bear.You are dead."
    elif berry == "2":
        print "You woke up in bed next to you was MorFiuse."
        
raw_input("The game is over, please click on the enter to close the window.")
