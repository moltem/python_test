import json
class Json2Html:

##
    def task_1_json2html(json_file_path: str)-> str: 
        
        if json_file_path is None or json_file_path == "":
            raise ValueError('json_file_path is empty')

        mapping_dict = {"title":"<h1>","body":"<p>"}
        html_template = "<h1>{title}</h1><p>{body}</p>"    
        list_tag = set(mapping_dict.keys())
        html=""

        try:
            with open(json_file_path,"r") as file:            
                for d in json.load(file):
                    if(set(d.keys()) == list_tag):
                        html = html + html_template.format(**d)
                    else:
                        raise ValueError('html_template and json_file have different number of parameters.')
        except Exception as e:
            raise ValueError('Can\t read JSON file.')

        return html  

##
##
    def task_2_json2html(json_file_path: str)-> str:

        if json_file_path is None or json_file_path == "":
            raise ValueError('json_file_path is empty')

        html=""

        try:
            with open(json_file_path,"r") as file:
                for dic_line in json.load(file):
                    for key in dic_line:
                        html= html + "<"+key+">"+dic_line[key]+"</"+key+">"

        except Exception as e:
            raise ValueError(e)

        return html
##
##
   
    def get_ul_line(json_data: list)-> str:

        html=""

        for line in json_data:
            if(isinstance(line,dict)):   
                html= html + get_li_line(line)

            elif (isinstance(line,list)):
                html= get_ul_line(line)

            else:
                html= html + "<li>"+ line + "</li>"

        return "<ul>" + html + "</ul>"

##
    def get_li_line(dic_line: dict)-> str:

        html=""

        for key in dic_line:
            if(isinstance(dic_line[key],list)):
                html= html +"<"+key+">"+get_ul_line(dic_line[key])+"</"+key+">"

            else:
                html= html +"<"+key+">"+dic_line[key]+"</"+key+">"

        return "<li>" + html + "</li>"

##
    def task_3_4_json2html(json_file_path: str)-> str:

        if json_file_path is None or json_file_path == "":
            raise ValueError('json_file_path is empty')
 
        try:

            with open(json_file_path,"r") as file:        
                json_data = json.load(file)
                html=""
                if(isinstance(json_data,list)):
                    html = get_ul_line(json_data)

                elif(isinstance(json_data,dict)):
                    html = "<ul>" + get_li_line(json_data) + "</ul>"

                else:    
                    html = json_data

        except Exception as e:
            raise ValueError(e)

        return html
##
##
    def get_list_line(json_data: list)-> str:

        html=""

        for line in json_data:

            if(isinstance(line,dict)):   
                html= html + get_dic_line(line)

            elif (isinstance(dic_line,list)):
                html= get_list_line(line)

            else:
                html= html + line

        return html


    def get_dic_line(dic_line: dict)-> str:

        html=""

        for key in dic_line:

            tag_dict = dict()
            class_list = []
            id_list = []

            if(isinstance(dic_line[key],list)):
                html= html +"<"+key+">"+get_ul_line(dic_line[key])+"</"+key+">"

            else:
                list_key = key.split(".")

                for elem in list_key:

                    if "#" in elem:
                        (cls,id_attr) = elem.split("#")
                        id_list.append(id_attr)
                        class_list.append(cls)

                    elif list_key.index(elem)==0:
                        tag = elem

                    else:
                        class_list.append(elem)

                str_id=""
                str_class=""

                if (bool(id_list)):
                    str_id = " id=\""+" ".join(id_list) +"\""
                if (bool(class_list)):
                    str_class = " class=\""+" ".join(class_list) +"\""

                html= html + "<" + tag + str_id + str_class + ">\"" + dic_line[key] + "\"</" + tag + ">"

        return html


    def task_5_json2html(json_file_path: str)-> str:

        if json_file_path is None or json_file_path == "":
            raise ValueError('json_file_path is empty')

        html=""

        try:

            with open(json_file_path,"r") as file:        
                json_data = json.load(file)
                if(isinstance(json_data,list)):
                    html = html + get_list_line(json_data)

                elif(isinstance(json_data,dict)):
                    html =  html + get_dic_line(json_data)

                else:    
                    html = html + json_data

        except Exception as e:
            raise ValueError(e)

        return html