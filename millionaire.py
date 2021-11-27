#Who wants to be a millionaire game. 
"""

Question number	Question value
1	£100
2	£200
3	£300
4	£500
5	£1,000 * guranteed cash
6	£2,000
7	£4,000
8	£8,000
9	£16,000
10	£32,000 * guranteed cash
11	£64,000
12	£125,000
13	£250,000
14	£500,000
15	£1,000,000
"""
# Greeting

print("Hello, what's your name?")
name = input()
print("Do you want to be a millionaire " + name + "?")
answer = input("Y/N ")
answer.upper()
if answer == "Y":
    print("Then lets play! Good luck!")
else:
    print("Then you should play another game. Goodbye!")

questions_answers = {"£100": ["Who was elected President of the United States in 2017?", "1. Donald Trump", "2. Barack Obama", "3. George Bush", "4. Abraham Lincoln", "*Donald Trump"],
"£200": ["Which religion believes in One God and the last prophet Muhammad?", "1. Buddhism", "2. Islam", "3. Hinduism", "4. Janeism", "*Islam"], "£300": ["What is the currency of France?", "1. Franc", "2. Euro", "3. Riyal", "4. Rupees", "*Euro"],
"£400": ["What term is used for sweet dishes in English?", "1. Savory", "2. Sour", "3. Dessert", "4. Aperterif", "*Dessert"],
"£500": ["How many colours in the Rainbow?", "1. One", "2. Five", "3. Two", "4. Seven", "*Seven"], 
"£600": ["Saudi Arabia is the biggest producer of what?", "1. Oil", "2. Coal", "3. Coffee", "4. Heroin", "*Oil"], 
"£700": ["What are the official languages of Canada?", "1. Dutch and French", "2. English and French", "3. French only", "4. English and Dutch", "*English and French"]}





