import yaml

# data = {"name": "zhangsan", "age": 12}
data = {"name": "张三", "age": 12}
with open("../data/write.yaml", "w", encoding="utf-8")as f:
    yaml.dump(data, f,allow_unicode=True)
