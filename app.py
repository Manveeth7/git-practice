def greet(name):
    return f"Greetings, {name}! Hope you're doing well."

def farewell(name):
    return f"Goodbye, {name}! Take care."

def shout(name):
    return f"HEY {name.upper()}!!"

def whisper(name):
    return f"...psst, {name}..."

if __name__ == "__main__":
    print(greet("Claude"))
    print(shout("Claude"))
    print(whisper("Claude"))
    print(farewell("Claude"))
