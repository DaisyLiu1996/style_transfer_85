import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
from util.visualizer import Visualizer


if __name__ == '__main__':
    opt = TestOptions().parse()
    opt.num_threads = 0
    opt.batch_size = 1
    opt.serial_batches = True
    opt.no_flip = True
    opt.display_id = -1
    dataset = create_dataset(opt)
    model = create_model(opt)
    model.setup(opt)
    
    visualizer = Visualizer(opt)
    visualizer.reset()

    if opt.eval:
        model.eval()
    for i, data in enumerate(dataset):
        print(i)
        if i >= opt.num_test:
            break
        model.set_input(data)
        model.test()
        visuals = model.get_current_visuals()
        img_path = model.get_image_paths()
   
        visualizer.display_current_results(visuals, i, 0)
        
