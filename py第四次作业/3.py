ls = ["Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", "Comprehensive",
      "Comprehensive", "Comprehensive", "Comprehensive", "Comprehensive", "Comprehensive",
      "Normal", "Polytechnic", "Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive",
      "Comprehensive", "Comprehensive", "Comprehensive", "Polytechnic", "Polytechnic", "Polytechnic", "Polytechnic",
      "Normal", "Comprehensive",
      "Agricultural and Forestry", "Polytechnic", "Comprehensive", "Polytechnic", "Polytechnic",
      "Polytechnic", "Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive",
      "Polytechnic", "Agricultural and Forestry", "Nationalities", "Military"]
# print(a)
d = {}
for word in ls:
    d[word] = d.get(word, 0) + 1
# 计数
d_sorted = sorted(d.items(), key=lambda v:v[0])
d = dict(d_sorted)
# 排序
for k in d:
    print("{} {}".format(k, d[k]))
