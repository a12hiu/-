import yaml


def analyze_data(file_name, case_name):
    with open("./data/"+file_name+".yaml", "r") as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
        res = list()
        res.extend(content[case_name].values())
        return res
