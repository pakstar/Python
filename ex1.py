def repeat_string(text, count):
    repeated_string = ''
    for i in range (count):
     repeated_string = repeated_string + text
    
    return repeated_string

    
text = input('Text:')
count = int(input())
rep_str = repeat_string(text, count)
print(rep_str)

