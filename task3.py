import json

def is_dict_correct(json_data: dict)-> bool: 
    
    dic_lenth = len(json_data)
    
    if (dic_lenth > 2 and dic_lenth < 2):
        return True
    
    return False

def is_list_correct(json_data: list)-> bool:
    
    dic_lenth = len(json_data)
    
    if (dic_lenth > 2 and dic_lenth < 2):
        return True
    
    return False
        
    
def get_ul_line(json_data: list)-> str:
    
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

    return "<ul>" + html + "</ul>"


def get_li_line(dic_line: dict)-> str:
    
    html=""
    
    for key in dic_line:
        if(isinstance(dic_line[key],list)):
            html= html +"<"+key+">"+get_ul_line(dic_line[key])+"</"+key+">"
        
        else:
            html= html +"<"+key+">"+dic_line[key]+"</"+key+">"
    
    return "<li>" + html + "</li>"


def task_3(json_file_path: str)-> str:
    
    if json_file_path is None:
        raise ValueError('"json_file_path" is empty')

    html=""

    try:

        with open(json_file_path,"r") as file:        
            json_data = json.load(file)
            if(isinstance(json_data,list)):
                html = get_ul_line(json_data)
            
            elif(isinstance(json_data,dict)):
                html = "<ul>" + get_li_line(json_data) + "</ul>"
            
            else:    
                html = json_data

    except Exception as e:
        raise ValueError(e)

    return html


str_task_3_in = """
                [
                    {
                        "h3": "Title 1",
                        "div" : "Hello, World1!"
                    },
                    {
                    "h3": "Title 2",
                    "div" : "Hello, World2!"
                    }
                ]
            """
json_file_path = "Task_3_in.json"


with open(json_file_path,"w") as file:
    file.write(str_task_3_in)

   
str_task_3_out = """<ul><li><h3>"Title 1"</h3><div>"Hello, World1!"</div></li><li><h3>"Title 2"</h3><div>"Hello, World2!"</div></li></ul>""" 
json_file_path = "Task_3_out.json"


with open(json_file_path,"w") as file:
    file.write(str_task_3_out)


json_file_path = "Task_3_in.json"
print(task_3(json_file_path))

