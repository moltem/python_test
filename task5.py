import json
        
    
def get_list_line(json_data: list)-> str:
    
    html=""
    
    for line in json_data:
        
        if(isinstance(line,dict)):   
            if(is_dict_correct(json_data)):
                raise ValueError('"get_ul_line.line" has wrong number of elements')
            html= html + get_li_line(line)
        
        elif (isinstance(dic_line,list)):
            html= get_ul_line(line)
             
        else:
            html= html + "<li>"+ line + "</li>"

    return html


def get_dic_line(dic_line: dict)-> str:
    
    html=""

    
    for key in dic_line:
        
        tag=""
        class_list = []
        id_list = []
        
        if(isinstance(dic_line[key],list)):
            html= html +"<"+key+">"+get_ul_line(dic_line[key])+"</"+key+">"
        
        else:
            list_key = key.split(".")
            
            for elem in list_key:
                
                if "#" in elem:
                    id_list.append(replace(elem,"#",""))
                
                elif list_key.index(elem)==0:
                    tag = elem
                
                else:
                    class_list.append(elem)
                            
            
            if not class_list:
                
                str1 = ''.join(str(e)+" " for e in list1
                html= html +"<"+key+">"+dic_line[key]+"</"+key+">"
    
    return html


def task_5(json_file_path: str)-> str:
    
    if json_file_path is None:
        raise ValueError('"json_file_path" is empty')

    html=""

    try:

        with open(json_file_path,"r") as file:        
            json_data = json.load(file)
            if(isinstance(json_data,list)):
                html = get_list_line(json_data)
            
            elif(isinstance(json_data,dict)):
                html =  get_dic_line(json_data)
            
            else:    
                html = json_data

    except Exception as e:
        raise ValueError(e)

    return html


str_task_5_in = """
                    {
                        "p.my-class#my-id": "hello",
                        "p.my-class.my-class2":"example<a>asd</a>" 
                    }
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

