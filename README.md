# style_transfer_85

## Description

This is project style_transfer developed by team 285_little composed of Haiya Ye, Ke Liu, Yifan Hou, Shijun Xu.

## Requirements

Install package 'imageio' as follow:
$ pip install --user imageio

## Code organization

demo.ipynb -- Run a demo of our code (reproduce result of cycleGAN)\
train.py -- train a cycleGAN model, we can use\
```js
python train.py --dataroot ./datasets/vangogh2photo --name your_name --model cycle_gan --gpu_ids 0 --batch_size 2 --niter 10 --niter_decay 20 --result_dir ./your_dir
```
test.py -- test images using a given cycleGAN model, we can use
```js
python test.py --dataroot ./datasets/vangogh2photo --name the given model name --model cycle_gan --result_dir ./your_test_dir/ --num_test 50
```

tranfer_style.ipynb -- this jupyter notebook implement original paper by Gatys on Neural Style Transfer \

util/ --Contains get_data.py (load data to a given dir), image_pool.py(preprocessing data), print_loss.ipynb(print loss from the loss_log.txt), visualizer.py(save images loss during training process) \

result_pickout -- some results that are produced by cycleGAN and also shown in our report \

options -- deal with the paramater options used during training and testing process\

models/__init__.py -- create a basic model by given options\
models/base_model.py -- class of abstract model define some basic methods to save losses and networks\

models/cycle_gan_model.py -- cycleGAN model inherit from base_model\
models/networks.py -- defined generater and discriminator classes which is used by cycleGAN model\
models/test_model.py -- test models used in test.py and demo.ipynb\

datasets/vangogh2photo -- testA: painting for test, testB: landscape for test, trainA: painting for train, trainB: landscape for train \

dataset_base -- 2 chosen paintings and landscapes for Neural style transfer(task1) \
data/ -- This is a dataloader, crops, normalizes, fetch data from given datasets\
