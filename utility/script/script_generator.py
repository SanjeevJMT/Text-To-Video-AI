import os
from openai import OpenAI
import json

OPENAI_API_KEY = os.getenv('OPENAI_KEY')
model = "gpt-4o-mini"
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_script(topic):
    prompt = (
        """You are a seasoned content writer for a YouTube channel, specializing in facts videos. 
        Your facts are concise, each lasting about 300 seconds (approximately 840 words). 
        They are incredibly engaging and original. When a user requests a specific type of facts short, you will create it.

        For instance, if the user asks for:
        Weird facts
        You would produce content like this:

        Weird facts you don't know:
        - Bananas are berries, but strawberries aren't.
        - A single cloud can weigh over a million pounds.
        - There's a species of jellyfish that is biologically immortal.
        - Honey never spoils; archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.
        - The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.
        - Octopuses have three hearts and blue blood.
        - Penguins waddle because their legs are shorter than their bodies and are positioned further back.
        - There are more trees on Earth than stars in our galaxy.
        - A day on Venus is longer than a year on Venus.
        - There's a place in Antarctica called "Blood Falls" where iron-rich saltwater flows out of the Taylor Glacier, making it look like blood is oozing from the ice.
        - Astronauts can grow taller in space.
        - The human nose can recognize over a trillion different scents.
        - There's a species of frog that can freeze itself solid during the winter and then thaw out in the spring.
        - The average person will spend six months of their life waiting at red lights.
        - There's a type of cloud called "lenticular clouds" that looks like flying saucers.
        - The world's oldest profession is believed to be prostitution.
        - Pigs can't look up at the sky.
		- There are more trees on Earth than stars in the Milky Way galaxy.
		- A day on Venus is longer than a year on Venus.
		- Astronauts can grow taller in space.
		- The human nose can recognize over a trillion different scents.
		- There's a species of frog that can freeze itself solid during the winter and then thaw out in the spring.
		- The average person will spend six months of their life waiting at red lights.
		- There's a type of cloud called "lenticular clouds" that looks like flying saucers.
		- There's a species of snail that has a penis longer than its own body.
		- The average person swallows about eight spiders in their sleep during their lifetime. (This is a common myth and likely untrue)
		- There's a type of bacteria that can survive in outer space.
		- The longest word in the English language has over 189,000 letters.
		- There are more possible games of chess than there are atoms in the observable universe.
		- The human brain generates more electrical activity when asleep than when awake.
		- The world's smallest mammal is the bumblebee bat, which can fit in the tip of your finger.
		- There's a type of cloud called "mammatus clouds" that looks like hanging breasts.
		- The first man to go to space, Yuri Gagarin, was only 27 years old.
		- The average person takes about 2,000 steps per day.
		- The world's largest living organism is a giant honey fungus in Oregon that covers over 2,200 acres.
		- The human body sheds about 600,000 particles of skin every hour.
		- There's a species of fish that can "walk" on land.
		- The Mona Lisa has no eyebrows.
		- The first movie ever made with sound was "The Jazz Singer" in 1927.
		- The tallest mountain in the solar system is Olympus Mons on Mars, which is almost three times taller than Mount Everest.
		- The world's largest living thing is a giant sequoia tree named "General Sherman" in California.
		- There's a type of ice cream called "Durian Ice Cream," which is made with the durian fruit, known for its strong, pungent odor.
		- The first computer was the size of a room.
		- The average person blinks about 15-20 times per minute.
		- The world's largest desert is the Antarctic Desert.
		- The first Olympic Games were held in 776 BC in Greece.
		- The human brain can store an estimated 2.5 petabytes of information.
		- The first cell phone was invented in 1973.
		- The world's longest river is the Nile River in Africa.
		- The first book printed on a printing press was the Gutenberg Bible.
		- The world's largest ocean is the Pacific Ocean.
		- The first airplane flight was in 1903 by the Wright brothers.
		- The human body contains more bacteria than human cells.
		- The world's largest land animal is the African elephant.
		- The first television broadcast was in 1928.
		- The world's largest bird is the ostrich.
		- The first car was invented in 1885.
		- The world's largest island is Greenland.
		- The first person to walk on the moon was Neil Armstrong in 1969.
		- The world's largest mammal is the blue whale.
		- The first internet website was created in 1991.
		- The world's largest volcano is Mauna Loa in Hawaii.
		- The first video game was created in 1958.
		- The world's largest cave system is the Mammoth Cave System in Kentucky.
		- The first artificial satellite to orbit the Earth was Sputnik 1 in 1957.
		- The world's largest living organism is a giant honey fungus in Oregon that covers over 2,200 acres.
		- The first nuclear bomb was detonated in 1945.
		- The world's largest waterfall is Iguazu Falls on the border of Brazil and Argentina.
		- The first human in space was Yuri Gagarin in 1961.
		- The world's largest ocean animal is the blue whale.
		- The first computer virus was created in 1983.
		- The world's largest land animal is the African elephant.
		- The first person to climb Mount Everest was Sir Edmund Hillary in 1953.

        You are now tasked with creating the best short script based on the user's requested type of 'facts'.

        Keep it brief, highly interesting, and unique.

        Stictly output the script in a JSON format like below, and only provide a parsable JSON object with the key 'script'.

        # Output
        {"script": "Here is the script ..."}
        """
    )

    response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": topic}
            ]
        )
    content = response.choices[0].message.content
    try:
        script = json.loads(content)["script"]
    except Exception as e:
        json_start_index = content.find('{')
        json_end_index = content.rfind('}')
        print(content)
        content = content[json_start_index:json_end_index+1]
        script = json.loads(content)["script"]
    return script
