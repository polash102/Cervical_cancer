import kagglehub

dataset_id = "mohaliy2016/papsinglecell"

path = kagglehub.dataset_download(dataset_id)

print("Dataset downloaded to:")
print(path)
