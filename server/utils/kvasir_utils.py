kvasir_label_index = {
    'dyed-lifted-polyps': 0,
    'dyed-resection-margins': 1,
    'esophagitis': 2,
    'normal-cecum': 3,
    'normal-pylorus': 4,
    'normal-z-line': 5,
    'polyps': 6,
    'ulcerative-colitis': 7
}

kvasir_index_label = {
    0: 'dyed-lifted-polyps',
    1: 'dyed-resection-margins',
    2: 'esophagitis',
    3: 'normal-cecum',
    4: 'normal-pylorus',
    5: 'normal-z-line',
    6: 'polyps',
    7: 'ulcerative-colitis'
}

def encode_predictions(predictions):
    """ Encode kvasir prediction

        # Returns
            dict with class ids and predictions
    """
    return {kvasir_label_index[label]: probability 
        for label, probability in predictions.iteritems()}

def decode_predictions(predictions):
    """ Decode kvasir prediction

        # Returns
            dict with class labels and predictions
    """
    return {kvasir_index_label[index]: probability 
        for index, probability in predictions.iteritems()}

