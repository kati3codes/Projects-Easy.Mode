import time

phrase = "Python is the best coding language."
word_count = len(phrase.split())

print(f"Type this fast: \n{phrase}\n")
input("Press enter to start.")

start_time = time.time()
attempt = input("Type here: ")
end_time = time.time()

time_taken = (end_time - start_time) / 60
wpm = round(word_count / time_taken, 2)

if attempt == phrase:
    print(f"\nSuccess! Your speed: {wpm} WPM")
else:
    print("Nope. Try again.")