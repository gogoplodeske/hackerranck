from data import Images

with Images('data\images.tar') as images:
    path = images.paths[0]
    image = images[path]
    print('read image "{}"" of shape {}'.format(path, image.shape))