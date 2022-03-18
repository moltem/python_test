import json

 

def task_2(json_file_path: str)-> str:
    
    if json_file_path is None:
        raise ValueError('"json_file_path" is empty')

    
    html_list_templates=[]
    html=""

    try:
        with open(json_file_path,"r") as file:
            for dic_line in json.load(file):
                for key in dic_line:
                    html= html + "<"+key+">"+dic_line[key]+"</"+key+">"
                html_list_templates.append(html)
    
    except Exception as e:
        raise ValueError(e)
    
    return html

 
str_task_2_in = """
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
json_file_path = "Task_2_in.json"

with open(json_file_path,"w") as file:
    file.write(str_task_2_in)

   
str_task_2_out = """<h3>"Title 1"</h3><div>"Hello, World1!"</div><h3> "Title 2"</h3><div>"Hello, World2!"</div>"""
json_file_path = "Task_2_out.json"

with open(json_file_path,"w") as file:
    file.write(str_task_2_out)

   
json_file_path = "Task_2_in.json"
print(task_2(json_file_path))