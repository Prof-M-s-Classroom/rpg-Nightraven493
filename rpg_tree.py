class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):
        #print(f"TODO: Initialize StoryNode with event_number={event_number}, description={description}")
        # TODO: Initialize instance variables (event_number, description, left, right)
        self.event_number = event_number
        self.description = description
        self.left = None
        self.right = None

class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):
        #print("TODO: Initialize an empty decision tree")
        self.nodes = {}
        self.root = None

    def insert(self, event_number, description, left_event, right_event):
        """Insert a new story node into the tree."""
        #print(f"TODO: Insert event {event_number} with description '{description}' into the tree")
        # TODO: Check if event_number exists in self.nodes, if not create a new StoryNode
        # TODO: Assign left and right children based on left_event and right_event
        # TODO: Set root if it's the first node inserted
        if (event_number not in self.nodes):
            newNode = StoryNode(event_number, description)
            newNode.left = left_event
            newNode.right = right_event
            self.nodes[event_number] = newNode
        
        if(len(self.nodes) == 1):
            self.root = newNode

    def play_game(self):
        """Interactive function that plays the RPG."""
        #print("TODO: Implement the game logic for traversing the decision tree")
        # TODO: Start from the root node
        # TODO: Loop through player choices, navigating left or right based on input
        # TODO: Print event descriptions and ask for player decisions
        # TODO: End game when reaching a leaf node (where left and right are None)
        print(self.root.description)
        inp = input()
        if(inp == '1'):
            currNode = self.nodes[self.root.left]
        elif(inp == '2'):
            currNode = self.nodes[self.root.right]
        else:
            print("Not an option, exiting....")
            exit()
        
        while(True):   
            print(currNode.description)
            inp = input()
            if(inp == '1'):
                if(currNode.left == '-1'):
                    print("You have reached the end of the story, exiting....")
                    exit()
                currNode = self.nodes[currNode.left]
            elif(inp == '2'):
                if(currNode.right == '-1'):
                    print("You have reached the end of the story, exiting....")
                    exit()
                currNode = self.nodes[currNode.right]
            else:
                print("Not an option, exiting....")
                exit()

def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    #print(f"TODO: Read story file '{filename}' and parse events")
    # TODO: Open the file and read line by line
    # TODO: Split each line into event_number, description, left_event, right_event
    # TODO: Call game_tree.insert() for each event to build the tree
    f = open("C:\\Users\\Natilus\\Documents\\Code\\CS496\\hw5\\rpg-Nightraven493\\aistory.txt", "r")
    for line in f:
        parts = line.strip().split("|")
        game_tree.insert(parts[0].strip(),parts[1].strip(),parts[2].strip(),parts[3].strip())
    f.close()

# Main program
if __name__ == "__main__":
    
    #print("TODO: Initialize the GameDecisionTree and load story data")
    game_tree = GameDecisionTree()

    #print("TODO: Load the story from 'story.txt'")
    load_story("story.txt", game_tree)

    #print(game_tree.nodes['1'].description)

    #print("TODO: Start the RPG game")
    game_tree.play_game()