# 读取data.xml并生成一个python对象，XML元素属性如需要作为python对象属性进行访问如：obj.name。
import xml.dom.minidom


class Xml(object):
    def __init__(self, xml_f):
        self.xml_f = xml_f

    @property
    def xname(self):
        # 打开xml文档
        dom = xml.dom.minidom.parse(self.xml_f)
        # 得到文档元素对象
        root = dom.documentElement
        print(root)
        ps = root.getElementsByTagName('p')
        for p in ps:
            if p.hasAttribute("name"):
                print(p.getAttribute("name"))


x = Xml('data.xml')
x.xname
