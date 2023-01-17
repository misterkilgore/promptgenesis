class PromptGenerator: 
    MAIN_TYPE = ['photo', 'painting']
    LIGHTING = ['soft', 'ambient', 'ring light', 'neon']
    ENVIRONMENT = ['indoor', 'outdoor', 'underwater', 'space']
    COLOR_SCHEME = ['vibrant', 'dark', 'pastel']
    POV = ['front', 'overhead', 'side']
    BACKGROUND = ['solid color', 'nebula', 'forest']
    ART_STYLE = ['3d render', 'studio ghibli', 'movie poster']
    PHOTO_STYLE = ['macro', 'telephoto']
    

    
    def __init__(self):
        pass
    
    def interactive_prompt(self):
        print('1. Do you want a photo or a painting?')
        print('2. What’s the subject of the photo? Person? An animal or perhaps a landscape?')
        print('''3. What details do you want to add?
        ○ Special Lighting. Soft, ambient, ring light, neon
        ○ Environment. Indoor, outdoor, underwater, in space
        ○ Color Scheme. Vibrant, dark, pastel
        ○ Point of view. Front, Overhead, Side
        ○ Background. Solid color, nebula, forest''')
        print('4. In a specific art style? 3D render, studio ghibli, movie poster')
        print('5. A specific photo type? Macro, telephoto')