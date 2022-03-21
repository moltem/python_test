import unittest

from Json2Html import Json2Html

 
class TestJson2Html(unittest.TestCase):
  

    def setUp(self):

        self.t1_json_file_path_in = "Task_1_in.json"

        self.t2_json_file_path_in = "Task_2_in.json"

        self.t3_json_file_path_in = "Task_3_in.json"

        self.t4_json_file_path_in = "Task_4_in.json"

        self.t5_json_file_path_in = "Task_5_in.json"

        self.json2Html = Json2Html()

        self.str_task_1_out = """<h1>Title #1</h1><p>Hello world 1!</p><h1>Title #2</h1><p>Hello world 2!</p>"""

        self.str_task_2_out = """<h3>"Title 1"</h3><div>"Hello, World1!"</div><h3>"Title 2"</h3><div>"Hello, World2!"</div>"""

        self.str_task_3_out = """<ul><li><h3>"Title 1"</h3><div>"Hello, World1!"</div></li><li><h3>"Title 2"</h3><div>"Hello, World2!"</div></li></ul>"""

        self.str_task_4_out = """<ul><li><span>"Title 1"</span><content><ul><li><p>"exampl 1"</p><header>"header1"</header></li></ul></content></li><li><div>"div 1"</div></li></ul>"""

        self.str_task_5_out = """<p id="my-id" class="my-class">hello</p><p class="my-class my-class2">example<a>asd</a></p>"""


    def test_task_1_json2html(self)-> str:

        self.assertEqual(self.json2Html.task_1_json2html(self.t1_json_file_path_in), self.str_task_1_out)

 
    def test_task_2_json2html(self)-> str:

        self.assertEqual(self.json2Html.task_2_json2html(self.t2_json_file_path_in), self.str_task_2_out)
       

    def test_task_3_json2html(self)-> str:

        self.assertEqual(self.json2Html.task_3_4_json2html(self.t3_json_file_path_in), self.str_task_3_out)
       

    def test_task_4_json2html(self)-> str:

        self.assertEqual(self.json2Html.task_3_4_json2html(self.t4_json_file_path_in), self.str_task_4_out)
       

    def test_task_5_json2html(self)-> str:

        self.assertEqual(self.json2Html.task_5_json2html(self.t5_json_file_path_in), self.str_task_5_out)

        

if __name__ == "__main__":

    unittest.main()

