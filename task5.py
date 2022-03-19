import json
        
    
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


def task_5(json_file_path: str)-> str:
    
    if json_file_path is None:
        raise ValueError('"json_file_path" is empty')

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


str_task_5_in = """[
                    {
                        "p.my-class#my-id": "hello",
                        "p.my-class.my-class2":"example<a>asd</a>" 
                        
                     },
                     {
                        "p.my2-class#my2-id": "hello",
                        "p.my2-class.my2-class2":"example<a>asd</a>" 
                        
                     }
                    ]
            """
json_file_path = "Task_5_in.json"


with open(json_file_path,"w") as file:
    file.write(str_task_5_in)

   
str_task_5_out = """<p id="my-id" class="my-class">hello</p><p class="my-class1 my-class2">example<a>asd</a></p>""" 
json_file_path = "Task_5_out.json"


with open(json_file_path,"w") as file:
    file.write(str_task_5_out)


json_file_path = "Task_5_in.json"
print(task_5(json_file_path))


