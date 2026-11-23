#what are the possible sentences?
#pick up brown bowl
#pick up the characteristic + object type.
#pick up == add to inventory of player but that is not to be included in this code cus thats player class stuff
#verb + article + noun = sentence structure


class Sentence:
    def __init__(self):
        #seperate self by spaces and assign variable of verb to first word, article to second word, adjective to third word, and noun to fourth word.
        self.verb = None
        self.article = None
        self.adjective = None
        self.noun = None
        self.output = None


    def parse(self, input):
        words = input.split(" ")
        if len(words) == 3:
            self.verb = words[0]
            self.article = words[1]
            self.noun = words[2]
        elif len(words) == 4:
            self.verb = words[0]
            self.article = words[1]
            self.adjective = words[2]
            self.noun = words[3]
        else:
            print("Invalid sentence structure. Please use 'verb article noun' format.")

            if self.verb == "pickup":
                self.pickup()

            if self.verb == "throw":
                self.throw()
            if self.verb == "eat" or self.verb == "drink":
                self.ingest()

            if self.verb == "go":
                self.go()

    def pickup(self):
        pass
        

    def throw(self):
        pass
        self.output == f" Oh sorry, but I am f{self.noun} intolerant"

    def go(self):
        pass