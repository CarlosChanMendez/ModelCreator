import os
import datetime

class Table:
    def __init__(self):
        self.name = ""
        self.items = []

class Item():
    def __init__(self):
        self.name = ""
        self.type = ""

class javaClassModel():
    def __init__(self,package):
        self.template = open(os.getcwd() + "/assets/templates/model.java")
        self.template_content = self.template.read()
        self.template.close()
        self.package = package
        self.classname = ""
        self.props = []
        self.methods = []
    
    def addVariable(self,item):
        var_name = item.name
        var_type = ""
        if item.type.count("int")>=1:
            var_type = "int"
        elif item.type.count("varchar")>=1:
            var_type = "String"
        else:
            var_type = "String"
        line = f"\tprivate {var_type} {var_name};"
        self.props.append(line)
    
    def addMethod(self,item):
        var_name = item.name
        var_type = ""
        if item.type.count("int")>=1:
            var_type = "int"
        elif item.type.count("varchar")>=1:
            var_type = "String"
        else:
            var_type = "String"
        template = open(f"{os.getcwd()}/assets/templates/setters_and_getters.java","r")
        template_content = template.read()
        template_content = template_content.replace("$VAR_NAME",var_name)
        template_content = template_content.replace("$VAR_TYPE",var_type)
        self.methods.append(template_content)
    
    def setClassName(self,name):
        date = datetime.datetime.now()
        date_text = f"{date.day}-{date.month}-{date.year} at {date.hour}:{date.minute}:{date.second}"
        self.template_content = self.template_content.replace("$PACKAGE",self.package)
        self.template_content = self.template_content.replace("$DATE",date_text)
        self.template_content = self.template_content.replace("$CLASSNAME",name)
        self.classname = name
    
    def setProps(self):
        props_string = ""
        for i in self.props:
            props_string += i + "\n"
        self.template_content = self.template_content.replace("$PROPS",props_string)
    
    def setMethods(self):
        methods_string = ""
        for i in self.methods:
            methods_string += i + "\n"
        self.template_content = self.template_content.replace("$METHODS",methods_string)
    
    def getJavaClassModel(self):
        return self.template_content
    
    def debug(self):
        print(self.template_content)

class dataAnalyze:
    def __init__(self,file,package):
        self.file = file
        self.package = package
    
    def importFile(self):
        with open(self.file,"r") as file:
            file_content = file.read()
            file_content = file_content.splitlines()
            text_file = ""
            for line in file_content:
                if line.startswith("/*"):
                    pass
                elif line.startswith("--"):
                    pass
                elif line.startswith("DROP"):
                    pass
                elif line.startswith("LOCK"):
                    pass
                elif line.startswith("UNLOCK"):
                    pass
                elif line.count("PRIMARY KEY")>0:
                    pass
                elif line.startswith(")"):
                    text_file += "--" + "\n"
                elif len(line)==0:
                    pass
                else:
                    text_file += line + "\n"
            list_tables = []
            tables = text_file.split("--")
            for table in tables:
                if len(table)<=1:
                    pass
                else:
                    list_tables.append(table)
            return list_tables
    
    def exportFiles(self,list_models):
        for model in list_models:
            with open(f"{os.getcwd()}/models/{model.classname}.java","w") as file:
                file.write(model.getJavaClassModel())
    
    def createModel(self,tables):
        list_models = []
        for table in tables:
            model = javaClassModel(package=self.package)
            model.setClassName(table.name)
            for item in table.items:
                model.addVariable(item)
                model.addMethod(item)
            model.setProps()
            model.setMethods()
            list_models.append(model)
            self.exportFiles(list_models)


    
    def searchTables(self):
        list_tables = []
        tables = self.importFile()
        for table in tables:
            new_table = Table()
            new_table.name = table.split(" ")[2].title().replace("_","").replace("`","")
            list_items = table.replace("` (","` -").split("-")[1].split(",")
            for item in list_items:
                if len(item)==1:
                    continue
                new_item = Item()
                new_item.name = item.split(" ")[2].replace("`","")
                new_item.type = item.split(" ")[3]
                new_table.items.append(new_item)
            list_tables.append(new_table)
        return list_tables
    
    def getTables(self):
        tables = self.searchTables()
        self.createModel(tables)