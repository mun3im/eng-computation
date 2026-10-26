#!/usr/bin/env python3
"""
Run every extracted listing and report which ones execute standalone.

Each script is run from its own folder, with a non-interactive matplotlib
backend, so plotting listings do not block. Scripts that call input(), that
continue an earlier listing, or that read a data file the book does not ship
are reported separately rather than counted as failures.

    python3 run_all.py            # all chapters
    python3 run_all.py chapter08  # one chapter
"""
import glob, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def main(argv):
    pattern = os.path.join(HERE, argv[1] if len(argv) > 1 else '*', '*.py')
    scripts = sorted(p for p in glob.glob(pattern)
                     if os.path.basename(p) != 'run_all.py')
    if not scripts:
        print(f"no scripts matched {pattern}")
        return 1

    env = dict(os.environ, MPLBACKEND='Agg')
    buckets = {'ok': [], 'needs input': [], 'needs earlier listing': [],
               'needs a data file': [], 'raises (by design)': [], 'other': []}

    for path in scripts:
        source = open(path).read()
        rel = os.path.relpath(path, HERE)
        if 'input(' in source:
            buckets['needs input'].append((rel, '')); continue
        try:
            run = subprocess.run([sys.executable, os.path.basename(path)],
                                 capture_output=True, text=True, timeout=120,
                                 cwd=os.path.dirname(path), env=env)
        except subprocess.TimeoutExpired:
            buckets['other'].append((rel, 'timed out')); continue

        if run.returncode == 0:
            buckets['ok'].append((rel, '')); continue

        lines = [l for l in run.stderr.strip().split('\n')
                 if l.strip() and not l.startswith(' ')]
        last = lines[-1] if lines else 'failed'
        by_design = any(k in source for k in
                        ('raises', 'BUGGY', 'off-by-one', 'LinAlgError'))
        if by_design:
            buckets['raises (by design)'].append((rel, last))
        elif 'FileNotFoundError' in last:
            buckets['needs a data file'].append((rel, last))
        elif 'NameError' in last or 'ModuleNotFoundError' in last:
            buckets['needs earlier listing'].append((rel, last))
        else:
            buckets['other'].append((rel, last))

    print(f"ran {len(scripts)} scripts\n")
    for name, items in buckets.items():
        print(f"{name:24} {len(items)}")
    for name in ('other', 'needs a data file'):
        if buckets[name]:
            print(f"\n--- {name} ---")
            for rel, msg in buckets[name]:
                print(f"  {rel}\n      {msg[:100]}")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
