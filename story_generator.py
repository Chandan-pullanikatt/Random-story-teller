import random

class StoryGenerator:
    """
    A class to generate random stories from provided components.
    """
    def __init__(self):
        """Initializes the StoryGenerator with data components."""
        self.when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
        self.who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
        self.name = ['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker']
        self.residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
        self.went = ['the cinema', 'the university', 'a seminar', 'school', 'the laundry']
        self.happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book']

    def generate(self):
        """
        Generates and returns a single random story.
        
        Returns:
            str: A randomly constructed story.
        """
        story = (
            f"{random.choice(self.when)}, a character named {random.choice(self.name)}, "
            f"who was {random.choice(self.who)}, that lived in {random.choice(self.residence)}, "
            f"went to {random.choice(self.went)} and {random.choice(self.happened)}."
        )
        return story

# --- Main Execution Block ---
if __name__ == "__main__":
    # 1. Create an instance of our generator
    generator = StoryGenerator()
    
    # 2. Use the instance to generate a story
    my_story = generator.generate()
    
    # 3. Print the result
    print(my_story)
