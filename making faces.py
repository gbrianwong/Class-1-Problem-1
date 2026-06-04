def convert(emoji):
    emoji = emoji.replace(":)", '🙂')
    emoji = emoji.replace(":(", '🙁')
    return emoji

def main():
    print(convert(input("Are you :) or are you :( ? ")))

main()