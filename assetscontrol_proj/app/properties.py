class Properties:

    properties = {}
    
    def read_properties(self):

        with open("application.properties", "r") as f:
            for line in f.readlines():
                key=line.split("=")[0].strip()
                value=line.split("=")[1].strip()
                self.properties[key] = value
        
        return self.properties
    