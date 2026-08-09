import numpy as np

def complete_box_params(times, amps=[], ints=[]):
    
    times = np.asarray(times)
    n_amps, n_ints = len(amps), len(ints)

    if not (n_amps == times.size or n_ints == times.size):
        raise ValueError('Either amps or ints must be provided and have the same length as times.')

    if n_amps == 0:
        ints = np.asarray(ints)
        amps = ints / times
    else:
        amps = np.asarray(amps)
    return times, amps


def make_box_kernel(rate, durs, amps=[], ints=[], pad=0):

    # Sanity-check parameters:
    durs, amps, ints = complete_box_params(durs, amps, ints)

    # Prepare kernel array:
    n = int(np.sum(durs) * rate)
    n += 2 * int(pad * rate)
    kernel = np.zeros(n)

    # Insert box lobes:
    for d, a in zip(durs, amps):
        pass
        kernel[int(t0 * rate):int(t1 * rate)] = a

    return kernel