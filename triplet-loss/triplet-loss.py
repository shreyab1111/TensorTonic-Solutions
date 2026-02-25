import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    anchor = np.array(anchor)
    positive = np.array(positive)
    negative = np.array(negative)
    d_pos = np.sum((anchor - positive) ** 2, axis=-1)
    d_neg = np.sum((anchor - negative) ** 2, axis=-1)

    loss = np.maximum(0, d_pos - d_neg + margin)

    return float(np.mean(loss))