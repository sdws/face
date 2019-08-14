# 读取data.json，取出所有值为数字的Key-Value对，按值从大到小排列，存入目标文件p2.txt
with open('data.json', 'rb') as fr:
    content_j = fr.read().decode('utf-8')
fr.close()
content_dict = eval(content_j)
dict_new = {}


def dict_v_num(d):
    for k, v in d.items():
        if isinstance(v, int):
            dict_new[k] = v
        elif isinstance(v, dict):
            dict_v_num(v)
        elif isinstance(v, list):
            for l in v:
                if isinstance(l, dict):
                    dict_v_num(l)
    return dict_new


print(dict_v_num(content_dict))
list_sort = sorted(dict_new.items(), key=lambda dict_new: dict_new[1], reverse=True)
with open('p2.txt', 'w') as fw:
    fw.write(str(list_sort))
fw.close()
print('保存成功')
