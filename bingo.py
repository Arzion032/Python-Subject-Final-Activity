import random

class Letter():
    def __init__(self,bingo_letter):
        self.items = []
        self.bingo_letter = bingo_letter
        
    def add_item(self, item):
        self.items.append(item)
        return f"Random Selected Number: {self.bingo_letter}-{item}"
        
    def show_list(self):
        return f"{self.bingo_letter}=> {', '.join(map(str, self.items))}"
    
# Specify the number ranges assigned to each letter in BINGO
ranges = {'B': range(1, 16), 'I': range(15, 31), 'N': range(30, 46), 'G': range(45, 61), 'O': range(60, 76)}
# Created a dictionary that maps each letter to corresponding range of numbers
all_num = {letter: list(ranges[letter]) for letter in ranges.keys()}

"""
This is what all_num looks like:
{
    'B': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
    'I': [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 
    'N': [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], 
    'G': [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], 
    'O': [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
}
"""

# Create a Letter object for each letter in "BINGO"
bingo = [Letter(letter) for letter in "BINGO"]
b_list, i_list, n_list, g_list, o_list = bingo

def play(message):
    
    while True:
        game = input(f"\n{message} ").upper()
        print()
        if game in ['Y','N']:
            break
        else:
            print("\nInvalid input. Please enter 'Y' or 'N'.\n")
            
    return game
   
# Game Loop
while True:
    
    print("START OF BINGO GAME!\n")
    
    while True:
        
        print("Available Numbers:")
        for avail_letter in all_num:
            print(f"{avail_letter}: {all_num[avail_letter]}")
        
        print("\nPicked Letters:")
        for picked_letter in bingo:
            print(picked_letter.show_list())
        
        if play("Do you want to pick a letter (Y/N)?") == 'Y':
            num_available = [item for value in all_num.values() for item in value]
            if num_available:
                chosen_number = random.choice(num_available)
                
                for avail, picked in zip(all_num, bingo):
                    if chosen_number in all_num[avail]:
                        all_num[avail].remove(chosen_number)
                        picked.add_item(chosen_number)
                        break
            else:
                print("No more numbers available to pick.")
                break
                
        else:
            print("This Bingo Game is Over!")
            
            break
        
    if play("Do you want to set another Bingo Game (Y/N)?") == 'Y':
        pass
    else: 
        print("""
                           Goodbye!
              --- Created by: Melvin Sarabia ---
        """)
        break
    
