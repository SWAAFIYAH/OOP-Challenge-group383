import time
import os
import sys
from random import choice

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5

		# Included 3 more attributes
        self.tricks = []
        self.action_history = []
        self.available_tricks = [ "sit", "roll over", "play dead", "shake hands", "fetch", "spin", "jump", "speak", "high five", "dance" ]
        
	# Function for animating the pet
    def animate_pet(self):
        frames = ["🐕", "🐶"]
        
        for _ in range(3):
            for frame in frames:
                sys.stdout.write(f'\r{frame} ')
                sys.stdout.flush()
                time.sleep(0.5)
                
        print("\n")

	# Function for loading animation
    def loading_animation(self, action):
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        
        for _ in range(5):
            for frame in frames:
                sys.stdout.write(f'\r{frame} {action}...')
                sys.stdout.flush()
                time.sleep(0.1)
                
        print("\n")

	# Eating function
    def eat(self):
        self.loading_animation(f"{self.name} is eating")
        
        if self.hunger <= 0:
            return f"{self.name} is not hungry!"
        
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        self.action_history.insert(0, "Ate food")
        
        return f"{self.name} enjoyed the meal!"

	# Sleeping function
    def sleep(self):
        self.loading_animation(f"{self.name} is sleeping")
        
        if self.energy >= 10:
            return f"{self.name} isn't tired!"
        
        self.energy = min(10, self.energy + 5)
        self.action_history.insert(0, "Took a nap")
        
        return f"{self.name} had a good sleep!"

	# Playing function
    def play(self):
        if self.energy < 2:
            return f"{self.name} is too tired to play! Try sleeping first."
        
        self.loading_animation(f"{self.name} is playing")
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        self.action_history.insert(0, "Played")
        
        return f"{self.name} had fun playing!"

	# Training function
    def train(self, trick_index):
        trick = self.available_tricks[trick_index - 1]
        
        if trick in self.tricks:
            return f"{self.name} already knows how to {trick}!"
        
        if self.energy < 2:
            return f"{self.name} is too tired to learn! Try sleeping first."
        
        self.loading_animation(f"{self.name} is learning to {trick}")
        self.tricks.append(trick)
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 1)
        self.action_history.insert(0, f"Learned {trick}")
        
        return f"{self.name} learned how to {trick}!"

	# Function to show tricks
    def show_tricks(self):
        if not self.tricks:
            return f"{self.name} doesn't know any tricks yet!"
        
        return f"{self.name}'s tricks: {', '.join(self.tricks)}"

	# Function to show pet's status
    def get_status(self):
        status = f"\n{self.name}'s Status:\n"
        status += f"Hunger:    {'⬛' * self.hunger}{'⬜' * (10-self.hunger)} ({self.hunger}/10)\n"
        status += f"Energy:    {'⬛' * self.energy}{'⬜' * (10-self.energy)} ({self.energy}/10)\n"
        status += f"Happiness: {'⬛' * self.happiness}{'⬜' * (10-self.happiness)} ({self.happiness}/10)\n"
        
        if self.action_history:
            status += "\nRecent actions:\n"
            
            for action in self.action_history[:4]:
                status += f"• {action}\n"
                
        return status

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
