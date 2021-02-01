from autoDM import InstaDM
import re
import instaloader

# Make instance
L = instaloader.Instaloader()

# Login or load session
L.login(your_username, your_password)  # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "csjuego")

# Make list of user's(my) followers
users_expressions = '''
'''
for followee in profile.get_followees():  # loop through user's(my) follwing list
    users_expressions += str(followee)

# Get usernames into a list
regEx = re.compile(r'<Profile\s(\w+)\s\(\d+\)>')    # use regex to get the user's profile name
mo = regEx.findall(users_expressions)    # creates list of usernames user(I) is(am) following

# Get bio of each followee
users_list = []    # list of users with wanted bio
wanted_bios = []    # list of wanted matches in bio (as strings)
user = ''   # check current user's (in current iteration) bio

for i in range(0,200):    # loop through the list of users and check their bio; longer range will take longer to process
    user = mo[i]
    user_profile = instaloader.Profile.from_username(L.context, mo[i])
    user_bio = (user_profile.biography).lower()    # get the user's bio 
    if any(match in user_bio for match in wanted_bios):    # check if any word in user's bio matches with wanted bios
        users_list.append(user)

if __name__ == '__main__':
    # Auto login
    insta = InstaDM(username=your_username, password=your_password, headless=False)

    # Send message
    for user in users_list:    # send message to everyone with wanted bios
        insta.sendMessage(user=user, message="hey!..")
