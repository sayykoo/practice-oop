import re

class UserSchem:
    pass

class DataBase:
    def get_data(self, url):
        with open(url, 'r', encoding='UTF-8') as f:
            result = f.readlines()
            f.close()
            return result
    
    def serializers(self, data):
        content = []
        for i in data:
            schema = dict()
            line = [i for i in re.split(r'\s', i) if i != '']
            for index in range(0, len(line)-1, 2):
                schema[line[index]] = line[index + 1]
            content.append(schema)
        return content
    
    
    
bd = DataBase()

print(bd.serializers(bd.get_data('112.txt')))