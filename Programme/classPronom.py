class Pronom:
    def __init__(self, pronom):
        self.pronom= pronom

    def e(self):
        if self.pronom=="il":
            return ""
        
        if self.pronom=="elle":
            return "e"

        if self.pronom=="iel":
            return "·e"


    def euse(self):
        if self.pronom=="il":
            return "re"
        
        if self.pronom=="elle":
            return "se"

        if self.pronom=="iel":
            return "r·euse"

    def eau(self):
        if self.pronom=="elle":
            return "elle"
        
        if self.pronom=="il":
            return "eau"

        if self.pronom=="iel":
            return "elleau"
    
    def maj(self):
        if self.pronom=="elle":
            return "Elle"
        if self.pronom=="iel":
            return "Iel"
        if self.pronom=="il":
            return "Il"


il=Pronom("il")
elle=Pronom("elle")
iel=Pronom("iel")



def pronom(pron):
    if pron=="il":
        pron=il
    if pron=="elle":
        pron=elle
    if pron=="iel":
        pron=iel
    return pron