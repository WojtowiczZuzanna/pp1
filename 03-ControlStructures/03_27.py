y = True
n = False

facebook = input("Do you have Facebook? (y/n) ")
if facebook == "y":
    facebook = True
else:
    facebook = False

twitter = input("Do you have Facebook? (y/n) ")
if twitter == "y":
    twitter = True
else:
    twitter = False

instagram = input("Do you have Facebook? (y/n) ")
if instagram == "y":
    instagram = True
else:
    instagram = False

if (facebook and twitter and instagram) == 1:
    print("A person can be a good influencer!")
elif facebook == 1 and twitter == 1 and instagram == 0:
    print("A person can be a good influencer!")
elif twitter == 1 and instagram == 1 and facebook == 0:
    print("A person can be a good influencer!")
elif instagram == 1 and facebook == 1 and twitter == 0:
    print("A person can be a good influencer!")
else: 
    print("A person can't be a good influencer")