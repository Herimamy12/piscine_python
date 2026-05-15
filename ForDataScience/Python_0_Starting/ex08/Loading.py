#!/usr/bin/env python3

"""A lightweight clone of tqdm implemented as `ft_tqdm`.

Provides a drop-in iterable wrapper with common options:
 - total, desc, leave, ncols, mininterval, unit, unit_scale, file

Usage:
    from Loading import ft_tqdm
    for x in ft_tqdm(range(100), desc='Processing'):
        ...
"""

import sys
import time
import shutil
from collections.abc import Iterable


def ft_tqdm(iterable=None, *, total=None, desc='', leave=True,
            ncols=None, mininterval=0.1, unit='it', unit_scale=False,
            file=None, ascii=False):
    """Return an iterator that displays a progress bar similar to tqdm.

    If `iterable` is None the returned object can be used in manual mode
    with `.update()` and `.close()`.
    """

    class _Tqdm:
        def __init__(self, iterable, total, desc, leave, ncols,
                     mininterval, unit, unit_scale, file, ascii):
            self.iterable = iterable
            self.total = total if total is not None else (len(iterable) if hasattr(iterable, '__len__') else None)
            self.desc = desc or ''
            self.leave = leave
            self.ncols = ncols
            self.mininterval = mininterval
            self.unit = unit
            self.unit_scale = unit_scale
            self.file = file or sys.stderr
            self.ascii = ascii

            self.n = 0
            self.start_t = None
            self.last_print = 0
            self.closed = False

        def __iter__(self):
            if self.iterable is None:
                raise TypeError('ft_tqdm iterable is None')
            self.start_t = time.time()
            for it in self.iterable:
                yield it
                self.update(1)
            self.close()

        def update(self, n=1):
            now = time.time()
            if self.start_t is None:
                self.start_t = now
            self.n += n
            if now - self.last_print >= self.mininterval or (self.total and self.n >= self.total):
                self.last_print = now
                self._display()

        def _display(self):
            try:
                bar = self._format_meter()
                print(bar, end='\r', file=self.file)
                self.file.flush()
            except Exception:
                pass

        def _format_meter(self):
            # determine terminal width
            if self.ncols is None:
                try:
                    self.ncols = shutil.get_terminal_size().columns
                except Exception:
                    self.ncols = 80

            elapsed = time.time() - (self.start_t or time.time())
            rate = (self.n / elapsed) if elapsed > 0 else 0.0

            if self.unit_scale:
                n_display = self._scale(self.n)
                rate_display = self._scale(rate)
            else:
                n_display = f"{self.n}"
                rate_display = f"{rate:0.2f}"

            if self.total:
                frac = min(float(self.n) / self.total, 1.0)
                pct = int(frac * 100)
                # reserve space for description, percent, counts and rate
                bar_width = max(10, self.ncols - len(self.desc) - 40)
                filled = int(bar_width * frac)
                if filled >= bar_width:
                    bar_str = '[' + '=' * bar_width + ']'
                else:
                    bar_str = '[' + '=' * filled + '>' + ' ' * (bar_width - filled - 1) + ']'

                eta = (self.total - self.n) / rate if rate > 0 else 0
                eta_str = self._format_time(eta)
                return f"{self.desc} {bar_str} {pct:3d}% {self.n}/{self.total} [{rate_display} {self.unit}/s, ETA {eta_str}]"
            else:
                elapsed_str = self._format_time(elapsed)
                return f"{self.desc} {self.n} {self.unit} [{rate_display} {self.unit}/s, {elapsed_str} elapsed]"

        def _format_time(self, seconds):
            try:
                s = int(seconds)
            except Exception:
                s = 0
            h = s // 3600
            m = (s % 3600) // 60
            s = s % 60
            if h:
                return f"{h:d}:{m:02d}:{s:02d}"
            else:
                return f"{m:02d}:{s:02d}"

        def _scale(self, num):
            units = ['', 'K', 'M', 'G', 'T']
            idx = 0
            n = float(num)
            while abs(n) >= 1000.0 and idx < len(units)-1:
                n /= 1000.0
                idx += 1
            return f"{n:3.1f}{units[idx]}"

        def clear_line(self):
            try:
                print(' ' * (self.ncols or 80), end='\r', file=self.file)
                self.file.flush()
            except Exception:
                pass

        def close(self):
            if not self.closed:
                if self.leave:
                    try:
                        print('', file=self.file)
                    except Exception:
                        pass
                else:
                    self.clear_line()
                self.closed = True

        def __enter__(self):
            self.start_t = time.time()
            return self

        def __exit__(self, exc_type, exc, tb):
            self.close()

    return _Tqdm(iterable, total, desc, leave, ncols, mininterval, unit, unit_scale, file, ascii)

