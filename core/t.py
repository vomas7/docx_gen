import os
import sys

# from core.ui_objects import Run

current_path = os.getcwd()
root_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(root_path)


#todo возможно стоит подумать как сделать мроще для понимания сборку элементов и без сборки si_
#todo короче нужно подумать как изначально принимать si_document или перевести blob в норм тему






from core.ui_objects.paragraph import Paragraph


p = Paragraph()
print(p._class_registry)