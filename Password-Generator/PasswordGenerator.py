import tkinter as tk
import random
import string

def generate_password(length):
    # Generate a random password of given length
    if length.isdigit():
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(int(length)))
        return password
    else:
        return 'Invalid length'

def validate_length(text):
    # Validate that the text is a positive integer
    if text == '':
        return True
    elif text.isdigit():
        return int(text) > 0
    else:
        return False

def invalid_length():
    # Display an error message if the text is not a positive integer
    label.config(text='Invalid length', fg='red')

# Create a window
window = tk.Tk()
window.title('Password Generator')
window.geometry('400x400')
window.configure(bg='#1a1a1a', padx=20, pady=20)

# Create a label for the entry
entry_label = tk.Label(window, text='Enter password length:', font=('Arial', 20), bg='#1a1a1a', fg='#f0f0f0')
entry_label.pack(side=tk.TOP, pady=10)

# Create an entry for the password length
pass_entry = tk.Entry(window, width=20, font=('Arial', 20), bg='#1a1a1a', fg='#f0f0f0', textvariable="")
pass_entry.pack(side=tk.TOP, pady=10)

# Add validation to the entry
pass_entry.config(validate='focusout', validatecommand=(window.register(validate_length), '%P'), invalidcommand=invalid_length)

# Create a label for the password
label = tk.Label(window, text='Password', font=('Arial', 20), bg='#1a1a1a', fg='#f0f0f0')
label.pack(side=tk.TOP, pady=10)

# Create a button to generate the password
button = tk.Button(window, text='Generate Password', font=('Arial', 20), bg='#1a1a1a', fg='#f0f0f0', command=lambda: label.config(text=generate_password(pass_entry.get()), fg='#f0f0f0'))
button.pack(side=tk.TOP, pady=10)

# Start the main loop
window.mainloop()