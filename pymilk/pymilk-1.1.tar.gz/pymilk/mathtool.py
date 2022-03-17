

def percent_to_float(text):
    ''' percent_to_float('3.5%') -> 0.035 '''
    if '%' in text:
        return float(text.replace('%', '')) / 100
    return float(text)
