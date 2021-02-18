import pixellib
from pixellib.custom_train import instance_custom_training
print(3)
vis_img = instance_custom_training()
vis_img.load_dataset("dataset")
vis_img.visualize_sample()