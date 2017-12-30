"""
file_ = open('years&months&images&count.txt', 'w+')
            file_.writelines(str(list_year) + '@' + str(list_month) + '@' + str(list_images) + '@' + str(count))
            file_.close()
open_f = open('years&months&images&count.txt', 'r')
    data = open_f.read().split('@')
    list_year = ast.literal_eval(data[0])
    list_month = ast.literal_eval(data[1])
    list_images = ast.literal_eval(data[2])
    count = ast.literal_eval(data[3])
    open_f.close()
"""