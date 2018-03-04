
KVASIR_CLASSIFICATION_LABELS = {
    0: 'dyed-lifted-polyps',
    1: 'dyed-resection-margins',
    2: 'esophagitis',
    3: 'normal-cecum',
    4: 'normal-pylorus',
    5: 'normal-z-line',
    6: 'polyps',
    7: 'ulcerative-colitis'
}

def decode_predictions(predictions):
    return {KVASIR_CLASSIFICATION_LABELS[index]: probability 
        for (index, probability) in enumerate(predictions)}

