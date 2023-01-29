import pandas as pd
import numpy as np
import json
import logging

class PromptGenerator: 
    
    def __init__(self, main_type='photo', history_file=None):
        self.tags = []
        self.main = main_type
        
        with open('promptgenesis/config.json') as config_file:
            self.config = json.load(config_file)
        
        self.history_file = 'history.txt' if history_file is None else history_file
        logging.basicConfig(filename=self.history_file, filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)    
    
    def get_config(self):
        return(self.config)
           
    def get_prompt(self):
        if len(self.tags) > 0:
            return ', '.join(self.tags)
        else:
            return None
    
    def add_tag(self, text):
        self.tags.append(text)
    
    def add_prefix(self, subject):
        if self.main_type == 'photo':
            self.add_tags('a photo of ' + subject)
        else:
            self.add_tags('a painting of ' + subject)
    
    def log(self,text):
        logging.info(text)
    
    def random_style(self, subject):
        self.add_prefix(subject)
        