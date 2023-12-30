from tkinter import messagebox, simpledialog, Tk

def get_Task():
    task = simpledialog.askstring('Tasks', "Do you want to encrypt pr descrypt?")
    return task



def get_message():
    message = simpledialog.askstring("Message", "Enter the secret message")
    return message 

def is_even(number):
    return number % 2 ==0

def get_even_letters(message):
    even_letters = []
    for i in range(0, len(message)):
        if is_even(i):
            even_letters.append(message[i])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for i in range(0, len(message)):
        if not is_even(i):
            odd_letters.append(message[i])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message == message + 'x'

    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)

    for i in range(0,int(len(message)/2)):

        letter_list.append(odd_letters[i])
        letter_list.append(even_letters[i])

    new_message = ''.join(letter_list)
    return new_message
    







root = Tk()


while True:
    task = get_Task()
    if task == 'encrypt':
        message = get_message()
        new_message = swap_letters(message)
        messagebox.showinfo("Message",f'Ciphertext of the secret message is {new_message}')
    elif task == 'descrypt':
        message = get_message()
        descrypt_message = swap_letters(message)
        messagebox.showinfo("Message",f'Plaintext of the secret message is {descrypt_message}')
    else:
        break

root.mainloop() #izvikva se postoqnno 








#askstring: dialog v koito shte ima zaglavie i dolu shte imame input 