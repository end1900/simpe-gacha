#naruto eye gacha              

import random
import time
gems = 1000
#laoding msgs
loadmsg = {
    "Awakening your inner power...": 10,
    "Focusing Chakra to the eyes...": 10,
    "Scanning ancient scrolls...": 10,
    "Consulting the Sage of Six Paths...": 10,
    "Manifesting the ritual circle...": 10
}

# eye list rarity (6 star = rarest, 1 star = most common)
s6 = ["Rinnegan", "Tenseigan"] #s6 = six star
s5 = ["Mangekyou Sharingan", "Eternal Mangekyou Sharingan"]
s4 = ["Sharingan (Three Tomoe)"]
s3 = ["Sharingan (Two Tomoe)", "Sharingan (One Tomoe)"]
s2 = ["Byakugan"]
s1 = ["normal eye"]
while gems >= 200:
#f string for gems -> prints gem amount with f string
    print(f"You have {gems} gems.")

    input("Press Enter to awaken your Doujutsu (200 gems)...")

    gems = gems - 200 # roll costs 200 gems

    roll = random.random()  # 0.0 to 1.0 for exact %

    if roll < 0.01:       # 1%  6 star (rarest)
        result = random.choice(s6)
    elif roll < 0.052:    # 4.2%  
     result = random.choice(s5)
    elif roll < 0.112:    # 6%  
     result = random.choice(s4)
    elif roll < 0.202:    # 9%  
        result = random.choice(s3)
    elif roll < 0.32:     # 11.8% 
        result = random.choice(s2)
    else:                 # 68%    1 star (most common)
        result = random.choice(s1)

    #RANDOM MESSAGE LOGIC RANDOM IDK WHY I DID THGIS ITS OTO MUCH WOOOOOOOORKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK!!!----------------------------------------------------------------------------------------------------------

# new weighted system
    st_list = list(loadmsg.keys())
    pt_luck = list(loadmsg.values())
    # revised
    pick =  random.choices(st_list, weights=pt_luck, k=2) #k is quantity, rooted in math

    m1 = pick[0]
    m2 = pick[1]

    while m2 == m1:
        m2 = random.choice(st_list)
    #penalty
    loadmsg[m1] = max(1, loadmsg[m1] - 5)
    loadmsg[m2] = max(1, loadmsg[m2] - 5)
#compensation - goes thru all messages and gives +1 pt
    for text in loadmsg:
        loadmsg[text] = loadmsg[text] + 1


    print(m1)
    time.sleep(1) #aaaaaaaaaaaaaaaa
    print(m2)
    time.sleep(0.7) #aaaaaaaaaaaaaaaa
    print("...")
    time.sleep(0.5) #aaaaaaaaaaaaaaaa
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if result in s6:
        print(f"YOU GOT A ★★★★★ STAR EYE! -> The {result}!!!", end= " ")
    elif result in s5:
        print(f"You awakened a ★★★★ star Eye! -> The {result}!", end=" ")
    elif result in s4:
        print(f"You awakened a ★★★ star Eye! -> The {result}.", end=" ")
    elif result in s3:
        print(f"You awakened a ★★ star Eye! -> The {result}.", end=" ")
    elif result in s2:
        print(f"You awakened a ★ star Eye! -> The {result}.", end=" ")
    else:
        print("The ritual is complete, but nothing has changed.")
    # eye result (flavor text)
    if result == "Rinnegan":
        print("The purple ripples expand in your eyes... You are now a God.")
    elif result == "Tenseigan":
        print("A flickering blue light consumes your vision! The moon is yours.")
    elif result == "Mangekyou Sharingan":
        print("The pain of loss triggers a transformation. Your pupils distressingly shift patterns.")
    elif result == "Eternal Mangekyou Sharingan":
        print("The pain of loss triggers a transformation. Your pupils shift patterns.")
    elif result == "Byakugan":
        print("Veins bulge around your temples! You see through all deception.")
    elif "Sharingan" in result:
        print(f"The Tomoe begin to spin... the Sharingan guides you.")
    else:
        print(f"You are left with a {result}."+ " Better luck next time.")


print("Your surroundings grow hazy... insufficient gems.")

