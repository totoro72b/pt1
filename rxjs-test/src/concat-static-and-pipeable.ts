import { concat, empty, interval } from 'rxjs';
import { concat as _concat, delay, startWith, take } from 'rxjs/operators';

/** concat - static creation version: create a new observable from 2 existing ones */
const interval$ = interval(500).pipe(delay(Math.floor(Math.random() * 1000)));
const source1$ = concat(interval$.pipe(take(3)), interval$);
source1$.subscribe(x => console.log('static version:', x)); // maintain order of execution

/** concat - pipeable version */
// delay a random interval, but concat will maintain original order
const delayed$ = empty().pipe(delay(Math.floor(Math.random() * 1000)));
delayed$
  .pipe(
    // pipeable concat operator. maintain order of execution
    _concat(
      delayed$.pipe(startWith('3...')),
      delayed$.pipe(startWith('2...')),
      delayed$.pipe(startWith('1...')),
      delayed$.pipe(startWith('GO'))
    ),
    startWith('Get ready...')
  )
  .subscribe(x => console.log('pipeable version', x));
