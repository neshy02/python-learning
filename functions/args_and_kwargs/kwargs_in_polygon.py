# https://stepik.org/lesson/567056/step/6?unit=561330

def get_data_fig(*args, **kwargs):
    p = sum(args)
    res = [p]
    params = ['tp', 'color', 'closed', 'width']
    for key in params:
        if key in kwargs:
            res.append(kwargs[key])
    return res