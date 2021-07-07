__Author__ = "Minux-Dev"
__APIName__ = "myDataBase"
__Version__ = "0.1"


try:
    from flask import Flask
    from flask_restplus import Resource, Api
    from scrap import Getting
except:
    "Failed importing modules!"

app = Flask(__name__)
api = Api(app)


class myFiles(Resource):
    def get(self, title):
        
        db = Getting(title=title)
        self.info, self.magnets = db.Show()
    
        jsonfile = list()
        for i in range(len(self.info)):
            jsonfile.append({"title": self.info[i],
                            "magnet": self.magnets[i]})

        with open(title+".csv", "w") as file:
            for link in jsonfile:
                #file.write(f"\nTitle: {link['title']}\nMagnet: {link['magnet']\n}")
                file.write("\nTitle: {} \n\nMagnet: {}\n".format(link['title'], link['magnet']))
                
        return jsonfile
                

api.add_resource(myFiles, "/minux/<string:title>")

if __name__ == "__main__":
    app.run()
