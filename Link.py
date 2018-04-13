class Link:        
    def __init__(self):
        self.link = ''
        self.found_on = []
    
    def __str__(self):
        return '{ ' + self.link + ' }'