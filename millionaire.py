#Who wants to be a millionaire game. 


# Greeting

print("Hello, what's your name?")
name = input()
print("\nDo you want to be a millionaire " + name + "?")
answer = input("Y? ")
print("\nThen lets play! Good luck!")


questions_answers = {"£100": ["Who was elected President of the United States in 2017?", "1. Donald Trump", "2. Barack Obama", "3. George Bush", "4. Abraham Lincoln", "*Donald Trump"],
"£200": ["Which religion believes in One God and the last prophet Muhammad?", "1. Buddhism", "2. Islam", "3. Hinduism", "4. Janeism", "*Islam"], "£300": ["What is the currency of France?", "1. Franc", "2. Euro", "3. Riyal", "4. Rupees", "*Euro"],
"£400": ["What term is used for sweet dishes in English?", "1. Savory", "2. Sour", "3. Dessert", "4. Aperterif", "*Dessert"],
"£500": ["How many colours in the Rainbow?", "1. One", "2. Five", "3. Two", "4. Seven", "*Seven"], 
"£1000": ["Saudi Arabia is the biggest producer of what?", "1. Oil", "2. Coal", "3. Coffee", "4. Heroin", "*Oil"], 
"£2000": ["What are the official languages of Canada?", "1. Dutch and French", "2. English and French", "3. French only", "4. English and Dutch", "*English and French"], 
"£4000": ["Which core ingredient is important to cook a savory dish?", "1. Salt", "2. Butter", "3. Sugar", "4. Flour", "*Salt"], 
"£8000": ["Which country is infamously known as Arch Rival of Pakistan?", "1. Afghanistan", "2. America", "3. India", "4. Spain", "*India"], 
"£16,000": ["When did Jonas Brothers make their musical comeback?", "1. 2011", "2. 2015", "3. 2020", "4. 2019", "*2019"], 
"£32,000": ["In 2016, which new type of chocolate was discovered?", "1. Ruby Chocolate", "2. Emerald Chocolate", "3. Diamond Chocolate", "4. Sapphire Chocolate", "*Ruby Chocolate"], 
"£64,000": ["Which popular Hollywood actor won the best actor Oscar award in 2016?", "1. Matt Damon", "2. Johnny Depp", "3. Leonardo Di Caprio", "4. Brad Pitt", "*Leonardo Di Caprio"], 
"£125,000": ["Which revolutionary march made feminism prominent in Pakistan?", "1. Feminist March", "2. Aurat March", "3. Mard March", "4. Freedom March", "*Aurat March"], 
"£250,000": ["In 1768, Captain James Cook set out to explore which ocean?", "1. Pacific Ocean", "2. Atlantic Ocean", "3. Indian Ocean", "4. Artic Ocean", "*Pacific Ocean"], 
"£500,000": ["What is the speed of sound approximately?", "1. 120km/h", "2. 1,200km/h", "3. 700km/h", "4. 900km/h", "*1,200km/h"], 
"£1,000,000": ["The phrase ”I think, therefore I am” was coined by which philosopher?", "1. Socrates", "2. Plato", "3. Aristotle", "4. Descartes", "*Descartes"]}

def game_over():
    print("Sorry that answer is incorrect. You lose.")   
    print ("Better luck next time.")


def display_questions():
    for prize, list in questions_answers.items():
        print("For {p}...".format(p=prize))
        print("\n")
        question = list[0]
        choices = list[1:5]
        print(question)
        print("\n")
        print(choices)
        print("\n")
        
        choice = input("\nType in your answer: ")
        print("\n")
    
        choice_star = "*"+ choice.title()
        if choice_star == list[-1]:
            print("\nCongratulations! You have won {p}".format(p=prize))
        else:
            break
    

             
display_questions()
game_over()


