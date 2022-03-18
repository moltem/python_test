import json

def json2html(json_file_path: str, mapping_dict: dict, html_template: str)-> str:
    
    if json_file_path is None:
        raise ValueError('json_file_path is empty')
    
    if not bool(mapping_dict) or mapping_dict is None:
        raise ValueError('mapping_dict is empty')
        
    if html_template is None:
        raise ValueError('html_template is empty')

        
    list_tag = set(mapping_dict.keys())

    html=""
    
    try:
        with open(json_file_path,"r") as file:
            list_data = json.load(file)
            for d in list_data:
                if(set(d.keys()) == list_tag):
                    html = html + html_template.format(**d)
    except Exception as e:
        print(e)
    
    return html  


def task_1_title_h1(json_file_path: str)-> str:
    
    mapping_dict = {"title":"<h1>","body":"<p>"}
    html_template = "<h1>{title}</h1><p>{body}</p>"
    return json2html(json_file_path, mapping_dict, html_template)
    

str_Task_1_in = """
                    [
                        {
                            "title":"Title #1",
                            "body":"Hello world 1!"     
                        },{
                            "title":"Title #2",
                            "body":"Hello world 2!"       
                        }
                    ]
                """
with open("Task_1_in.json",'w') as file:
    file.write(str_Task_1_in)

    
str_Task_1_out = """<h1>Title #1</h1><p>Hello world 1!</p><h1>Title #2</h1><p>Hello world 2!</p>"""
with open("Task_1_out.html",'w') as file:
    file.write(str_Task_1_out)    
    
json_file_path = "Task_1_in.json"
print(task_1_title_h1(json_file_path))



#3"Task_1_in.json"