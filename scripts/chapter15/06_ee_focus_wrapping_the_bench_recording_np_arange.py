"""
A First Look at Object-Oriented Python - EE Focus: Wrapping the Bench Recording
Source: chapters/chapter15.tex, line 350

Output as printed in the book:
    bench_rc voltage: 101 samples, 3 missing, v from 12.00 to 0.17 V
    bench_rc voltage: 101 samples, 0 missing, v from 12.00 to 0.17 V
    Measured tau: 0.4700 s
"""

t = np.arange(0, 2.001, 0.02)
v = 12.0 * np.exp(-t / 0.47)
v[40:43] = np.nan          # the three samples the logger lost near t = 0.8 s

rc = Signal(t, v, name="bench_rc voltage")
print(rc.summary())

rc.repair()
print(rc.summary())
print(f"Measured tau: {rc.time_constant():.4f} s")
