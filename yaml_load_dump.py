""" YAML load and dump """
import yaml

with open('sample.yaml', 'r') as f:
    doc = yaml.load(f)

print(yaml.dump(doc, indent=4))

