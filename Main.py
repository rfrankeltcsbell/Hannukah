foodlist={
    "Turkey":1,
    "Cranberry sauce":2,
    "Gravy":3,
    "Pumpkin Pie":2,
    "Sweet potato marshmellow":3,
    "Apple pie":5,
    "Cornbread dressing":4,
    "Stuffing":2,
    "bread roll":4,
    
   

}
print("fooditem")
for num,item in foodlist.items():
    print(f"we need {num},{item}")

    hklist={
        "Day 1":["Playstation"],
        "Day 2":["watch","toy"],
        "Day 3":["Necklace","money","jacket"],
        "Day 4":["tv","car","clothes""gift card"],
        "Day 5":["headphones","bracelet","ring","candy","flowers"],
        "Day 6":["Xbox","Nintendo Switch","computer","mouse","keyboard","PC"],
        "Day 7":["Mac","Surface","popcorn machine","cotton candy machine","keyboard","phone","chair"],
        "Day 8":["candles","monitor","cake","pool table","pinpong table","foosball table","dj booth table","dj mixer"],
        

    }
    print("hklist")
    for day,gifts in hklist.items():
        print(day)
        for gift in gifts: 
            print(f" -{gift}")