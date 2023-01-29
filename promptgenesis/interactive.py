def interactive_prompt():
    
    prompt = []
    
    print('1. Do you want a photo or a painting?')
    cur_input = input('> ')
    if cur_input:
        prompt.append(cur_input)
        
    print("What's the suject of the photo?")
    cur_input = input('> ')
    if cur_input:
        prompt.append(cur_input)
        
    print('''3. What details do you want to add?
    Special Lighting. Soft, ambient, ring light, neon
    Environment. Indoor, outdoor, underwater, in space
    Color Scheme. Vibrant, dark, pastel
    Point of view. Front, Overhead, Side
    Background. Solid color, nebula, forest''')
    cur_input = input('> ')
    if cur_input:
        prompt.append(cur_input)
        
    print('4. In a specific art style? 3D render, studio ghibli, movie poster')
    cur_input = input('> ')
    if cur_input:
        prompt.append(cur_input)
        
    print('5. A specific photo type? Macro, telephoto')
    cur_input = input('> ')
    if cur_input:
        prompt.append(cur_input)
    
    return prompt

print(interactive_prompt())