import openai
import os

openai.api_key = "removed to not leak key" #TODO: Paste your OPENAI Key here


def generate_rpg_story():
    client = openai.OpenAI(api_key=openai.api_key)

    prompt = """You are an expert narrative game designer. You will create a text-based branching narrative in a specific format. 
Each “event” in the narrative is on its own line, has the format:
<event_number> | <description> | <left_event> | <right_event>

Where:
1. <event_number> is an integer ID for the event (e.g., 1, 2, 3, …).  
2. <description> is a single sentence or multiple sentences describing the story at that point, and presents two choices to the reader labeled as “1)” and “2)”.  
3. <left_event> is the integer ID of the next event if the reader chooses “option 1” from the description, or -1 if it is an ending.  
4. <right_event> is the integer ID of the next event if the reader chooses “option 2” from the description, or -1 if it is an ending.

Important rules:
- Each event_number should be unique and strictly increasing (e.g., 1, 2, 3, ..., up to however many you choose).
- The story can have multiple branching paths. 
- DO NOT ADD LINES BETWEEN EVENTS
- Some branches should end, indicated by -1, meaning there is no further branching for that choice.
- The story should be coherent: references to future events must be valid, and the choices in the description should logically relate to those future events.
- **Do NOT** add any extra lines, commentary, or formatting outside of the described structure.
- Provide exactly N events (e.g., 12 events), each on its own line, strictly following the `<event_number> | <description> | <left_event> | <right_event>` format.
- In every event’s description, make sure to explicitly label the two choices with “1)” and “2)” to guide the reader.

The story’s setting: 
- A richly detailed science-fantasy realm where technology and magic blend together on an alien planet.
- The main character has just awakened or arrived in this world and is immediately faced with choices.
- Each event describes what the character sees, hears, or experiences, then offers two distinct choices labeled “1)” and “2)” that lead to different event numbers.

Please generate such a story now.""" # TODO: Prompt engineer to get the exact story format you want here.

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI that generates structured RPG stories."},
                  {"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content


def save_story_to_file(filename, story_text):
    #TODO: Store the generated text into story.txt
    file = open("C:\\Users\\Natilus\\Documents\\Code\\CS496\\hw5\\rpg-Nightraven493\\"+ filename, "w")
    file.write(story_text)

if __name__ == "__main__":
    story_text = generate_rpg_story()
    save_story_to_file("aistory.txt", story_text)