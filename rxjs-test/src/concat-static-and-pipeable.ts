import { of, concat, interval, empty } from 'rxjs';
import {
  take,
  startWith,
  endWith,
  concat as _concat,
  delay
} from 'rxjs/operators';
const numbers$ = of(1, 2, 3);

// append values to stream
numbers$
  .pipe(
    startWith('a', 'b', 'c'),
    endWith('d', 'e', 'f')
  )
  .subscribe(console.log);

// concat - static creation version
const interval$ = interval(500);
const source1$ = concat(interval$.pipe(take(3)), interval$);
source1$.subscribe(console.log); // maintain order of execution

//concat pipeable version
// delay a random interval
const delayed$ = empty().pipe(delay(Math.floor(Math.random() * 1000)));

delayed$
  .pipe(
    // pipeable concat operator. maintain order of execution
    _concat(
      delayed$.pipe(startWith('3...')),
      delayed$.pipe(startWith('3...')),
      delayed$.pipe(startWith('2...')),
      delayed$.pipe(startWith('1...')),
      delayed$.pipe(startWith('GO'))
    ),
    startWith('Get ready...')
  )
  .subscribe(console.log);
