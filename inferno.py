import random
def greet_and_introduce():
    response = ["Hi, I'm Infermo. I'm your app advisor. May i know your good name?",
    "it's Inferno, your app advisor. Could you tell me your name? "]
    print(random.choice(response))

def welcome(name):
    messages=["nice to meet you. How can i help you today?",
    "It's a pleasure meeting you. what would you like to know today?",
    ]
    print(random.choice(messages))

def show_menu():
    print("-----------------")
    print("These are the few areas that I can help with!")
    print("1.Gamming apps")
    print("2.Trading apps")
    print("3.Learing apps")
    print("4.Social apps")
    print("5.Data sharing apps")
    print("6.online shopping apps ")
    print("7.music apps")
    print("8.End this chat")
    print("-----------------")
    try:
        return int(input("enter your choice [1-8]:"))
    except:
        print("Can't find this option")

def gaming_app():
    print("-------------------------------------------")
    print("choose what type of gaming apps you need")
    print("1.Racing")
    print("2.Fighting")
    print("3.Story oriented")
    print("4.Puzzule")
    print("5.Card gamming")
    print("6.Battle arena")
    print("-------------------------------------------")
    choice = int(input("Enter your choice between[1-6]:"))
    if choice == 1 :
        print("These are top 5 racing games to get you occcupied")
        print("---------------------------------------------------")
        print("1.Asphalt 9: Legends \n2.Beach Buggy Racing 2 \n3.CSR Racing 2 \n4.Dirt Trackin’ 2 \n5.Grand Prix Story")
        print("---------------------------------------------------")
    elif choice == 2:
        print("These are top 5 fighting games to get you occcupied")
        print("---------------------------------------------------")
        print("1.Brawl Stars\n2.Clash of Robots\n3.EA Sports UFC\n4.Evoland 1 and 2\n5.Fighting Tiger – Liberal")
        print("---------------------------------------------------")
    elif choice == 3:
        print("These are top 5 story oriented games to get you occcupied")
        print("---------------------------------------------------")
        print("1.Lonewolf \n2.The Bard’s Tale \n3.Superbrothers: Sword & Sworcery EP \n4.OT Chronicles \n5.Banner Saga")
        print("---------------------------------------------------")

    elif choice == 4:
        print("These are top 5 puzzzle games to get you occcupied")
        print("---------------------------------------------------")
        print("1.All That Remains: Part 1 \n2.Amanita Design (Machinarium, Samorost 3)\n3.Blue Wizard Digital (Friday the 13th, Slayaway Camp) \n4.Bridge Constructor Portal \n5.Dear Villagers games (Bury Me, My Love, Another Lost Phone)")
        print("---------------------------------------------------")

    elif choice == 5:
        print("These are top 5 card games to get you occcupied")
        print("---------------------------------------------------")
        print("1. Hearthstone: Heroes of Warcraft \n2. Shadowverse \n3. Yu-Gi-Oh Duel Links \n4. Clash Royale \n5. Meteorfall: Journey")
        print("---------------------------------------------------")

    elif choice == 6:
        print("These are top 5 battle arena to get you occcupied")
        print("---------------------------------------------------")
        print("1. Arena of Valor. \n2. Brave Legends. \n3. Brawl Stars or Battle Bay. \n4. Heroes Arena. \n5. Heroes Evolved")
        print("---------------------------------------------------")
    else :
        print("it is not in the option")

def trade():
    print("Ah!! you want to peek into trading. Here are the few trading apps that could be useful for you")
    print("---------------------------------------------------")
    print("1.E*TRADE - Best Overall.\n2.TD Ameritrade - Best Trading Tools. \n3.Fidelity - Best for Everyday Investors. \n4.Interactive Brokers - Best for Professionals. \n5.TradeStation - Great for Active Traders.")
    print("---------------------------------------------------")

def learn():
    print("It's realy a great idea to learn. Here are few learning apps. I wish you to learn somethimg new and productive")
    print("---------------------------------------------------")
    print("1. UDEMY \n2. LYNDA \n3. KHAN ACADEMY \n4. TED \n5. LUMOSITY \n6. GOODREADS \n7. DUOLINGO")
    print("---------------------------------------------------")

def social():
    print("It's good to connect with others around the world. These apps could help you")
    print("---------------------------------------------------")
    print("1.Facebook \n2.Instagram \n3.Twitter \n4.Youtube \n5.Hike \n6.Hootsuite")
    print("---------------------------------------------------")

def data():
    print("So you need echange data with your friends.Below are the best working apps")
    print("---------------------------------------------------")
    print("AirDroid \n2.Superbeam \n3.Pushbullet \n4.Portal \n5.Xender \n6.BitTorrent Shoot \n7.WeTransfer")
    print("---------------------------------------------------")

def shopping():
    print("Are you a shopoholic.Here are some amazing apps for you to shop")
    print("---------------------------------------------------")
    print("1.Amazon App. \n2.Flipkart App. \n3.eBay App. \n4.Jabong App. \n5.Nykaa App. \n6.OLX App. \n7.Big Basket App.")
    print("---------------------------------------------------")

def music():
    print("My favourite song is 'Shape of you', what your's? here are the apps for")
    print("---------------------------------------------------")
    print("Spotify \n2.Apple Music \n3.Google Play Music \n4.YouTube Music \n5.Bandcamp \n6.Shazam \n7.Amazon Music \n8.Idagio ")
    print("---------------------------------------------------")

def inferno():
    greet_and_introduce()
    name=input("name: ")
    welcome(name)
    choice= show_menu()
    if choice == 8:
        print("I hope we meet soon, have a wonderful day")
    while(choice != 8):
        if choice == 1:
            gaming_app()
        elif choice == 2:
            trade()
        elif choice == 3:
            learn()
        elif choice == 4:
            social()
        elif choice == 5:
            data()
        elif choice == 6:
            shopping()
        elif choice == 7:
            music()
        else:
            print("I can't understand")
        choice = show_menu()
        if choice == 8:
            print("I hope we meet soon, have a wonderful day")
inferno()