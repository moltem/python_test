import Json2Html
########################################
#####################TASK1##############
########################################
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
#json_file_path = ""
print(Json2Html.task_1_json2html(json_file_path))


if str_Task_1_out != task_1_title_h1(json_file_path):
    raise ValueError('Results are different!')


#Tests:
#1) Wrong json_path
#2) 


########################################
#####################TASK2##############
########################################
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
print(Json2Html.task_2_json2html(json_file_path))

############################################
#####################TASK3##############
############################################

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
print(Json2Html.task_3_4_json2html(json_file_path))

############################################
#####################TASK4##############
############################################
str_task_4_in = """
                [
                    {
                        "span": "Title 1",
                        "content" : [{
                                        "p":"exampl 1",
                                        "header":"header1"
                                    }]
                    },
                    {"div" : "div 1"}
                ]
            """
json_file_path = "Task_4_in.json"


with open(json_file_path,"w") as file:
    file.write(str_task_4_in)

   
str_task_4_out = """<ul><li><span>"Title 1"</span><content><ul><li><p>"exampl 1"</p><header>header1</header></li></ul></content></li><li><div>"div 1"</div></li></ul>""" 
json_file_path = "Task_4_out.json"


with open(json_file_path,"w") as file:
    file.write(str_task_4_out)


json_file_path = "Task_4_in.json"
print(Json2Html.task_3_4_json2html(json_file_path))

############################################
#####################TASK5##############
############################################

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


