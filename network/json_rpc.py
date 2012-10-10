import network.socket_wrapper
import json

def get_answer(addr, method, params = None, get_error = False):
    if params is None:
        params = []

    obj = dict()
    obj['method'] = method
    obj['params'] = params
    obj['jsonrpc'] = '2.0'

    answer = json.loads(network.socket_wrapper.get_answer(addr, json.dumps(obj)))

    if 'result' in answer:
        result = answer['result']
    else:
        result = None

    if not get_error:
        return result

    if 'error' in answer:
        error = answer['error']
    else:
        error = None

    return result, error
