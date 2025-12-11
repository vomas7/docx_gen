import os
import sys

# from core.ui_objects import Run

current_path = os.getcwd()
root_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(root_path)


#todo возможно стоит подумать как сделать мроще для понимания сборку элементов и без сборки si_
#todo короче нужно подумать как изначально принимать si_document или перевести blob в норм тему






from core.ui_objects import Paragraph, Run, Text
from core.oxml_magic.parser import make_xml_tree, to_xml_str

p = Paragraph()
r1 = Run()
r2 = Run()
t1 = Text()
t2 = Text()
t21 = Text()


p.add(r1)
p.add(r2)
r1.add(t1)
r1.add(t2)
r2.add(t21)

tree = make_xml_tree(p)
print(to_xml_str(tree))
