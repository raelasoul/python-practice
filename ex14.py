from sys import argv

script, user_name, location = argv
prompt = '> '

print(f"Hi {user_name} from {location}. I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) # takes input from user using the prompt and stores it in variable 'likes'

print(f"I see that you are from {location}. Where do you currently live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")