def is_valid(a, b, c):
    """Base validation"""
    return validate_a(a)['is_valid'] and \
           validate(b)['is_valid'] and \
           validate(c)['is_valid']


def validate(param):
    """Validate parameter"""
    error = {'is_valid': True, 'msg': ''}
    try:
        int(param)
    except ValueError:
        error['is_valid'] = False
        error['msg'] = 'коэффициент не целое число'
    if param == '':
        error['is_valid'] = False
        error['msg'] = 'коэффициент не определен'
    return error


def validate_a(param):
    """Validate parameter a"""
    error = validate(param)
    if error['is_valid'] and int(param) == 0:
        error['is_valid'] = False
        error['msg'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    return error
