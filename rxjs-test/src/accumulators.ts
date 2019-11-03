console.clear();

import { interval } from 'rxjs';
import { reduce, scan, take } from 'rxjs/operators';

// const numbers$ = of(1, 2, 3, 4, 5);

const source$ = interval(1000); // emits 0, 1, 2, 3, ... at 1s interval

/** reduce: won't emit final value until observable completes */
const reducer$ = source$.pipe(
  take(3), // reduce will not emit w/o this
  reduce((acc, cur) => {
    return acc + cur;
  }, 0)
);
reducer$.subscribe(x => console.log('REDUCER: first 3 sums to', x));

// scan emits upon every source emission
const scanner$ = source$.pipe(
  scan((acc, cur) => {
    return acc + cur;
  }, 0)
);
scanner$.subscribe(x => console.log('SCANNER: sum', x));
