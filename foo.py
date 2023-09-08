from datasets import load_dataset

datasets = load_dataset("yilunzhao/robut", split="wtq")
print(datasets)

sample = datasets[10]
for k in sample:
    print(k)
    print(sample[k], '\n')