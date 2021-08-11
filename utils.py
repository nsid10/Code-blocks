def normalize(x, mode="minmax", a=None, b=None):
    """
    Feature scaling function for normalizing data

    Args:
        x (numpy.ndarray): Input data
        mode (str, optional): Type of normalization. Defaults to "minmax".
        a (int, optional): Lower bound in custom range. Defaults to None.
        b (int, optional): Upper bound in custom range. Defaults to None.
    """
    if mode == "minmax":
        # Min-max [0, 1]
        return (x - x.min(axis=0)) / (x.max(axis=0) - x.min(axis=0))
    if mode == "mean":
        # Mean normalization
        return (x - x.mean(axis=0)) / (x.max(axis=0) - x.min(axis=0))
    if mode == "standard":
        # Standardization
        return (x - x.mean(axis=0)) / x.std(axis=0)
    if mode == "custom":
        # Custom range [a, b]
        return a + ((x - x.min(axis=0)) * (b - a)) / (x.max(axis=0) - x.min(axis=0))
