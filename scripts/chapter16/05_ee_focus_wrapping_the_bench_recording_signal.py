"""
A First Look at Object-Oriented Python - EE Focus: Wrapping the Bench Recording
"""

import numpy as np

class Signal:
    """A time series of measurements, with the operations valid on it."""

    def __init__(self, t, v, name="signal"):
        self.t = np.asarray(t, dtype=float)
        self.v = np.asarray(v, dtype=float)
        self.name = name

    def n_missing(self):
        return int(np.isnan(self.v).sum())

    def repair(self):
        """Fill gaps by linear interpolation (Chapter 11)."""
        gaps = np.isnan(self.v)
        if gaps.any():
            self.v[gaps] = np.interp(self.t[gaps], self.t[~gaps], self.v[~gaps])
        return self

    def time_constant(self):
        """Recover tau from an exponential decay (Chapter 12)."""
        return -1 / np.polyfit(self.t, np.log(self.v), 1)[0]

    def summary(self):
        return (f"{self.name}: {self.t.size} samples, "
                f"{self.n_missing()} missing, "
                f"v from {self.v[0]:.2f} to {self.v[-1]:.2f} V")
