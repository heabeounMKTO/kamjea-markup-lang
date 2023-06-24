import os

class KMLmao():
    def __init__(self, htmlfile) -> None:
        self.html = htmlfile
        self.KML_DEF = {
            "សេចក្តីអធិប្បាយ":"html",
            "ទិន្នន័យគោល":"meta",
            "ចំណងជេីង":"title",
            "តំណ":"link",
            "រចនាបទ":"style",
            "សំណេរ":"script",
            "រូបភាព":"img",
            "ចែក":"div",
            "ក្បាល១":"h1",
            "ក្បាល២":"h2",
            "ក្បាល៣":"h3",
            "កថាខណ្ឌ":"p", 
            "តួសេចក្តី":"body"
        }
        self.outputdest = "dest"
        self.inputdest = "testsrc"
        pass


    def toKML(self):
        fuck= open(os.path.join(self.inputdest,self.html), "rt", encoding='utf-8') 
        fuck2 = open(os.path.join(self.outputdest, self.html), "wt", encoding='utf-8')
        
        for line in fuck.readlines():
            print(line)
            for index in range(0, len(self.KML_DEF)):
               if list(self.KML_DEF.keys())[index] in line:
                   x = list(self.KML_DEF.keys())[index]
                   print("found")
                   fuck2.write(line.replace(x , self.KML_DEF.get(x)))
               else:
                   print("not found") 
                
