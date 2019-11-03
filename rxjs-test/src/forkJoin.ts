import { forkJoin, fromEvent, interval } from 'rxjs';
import { take, tap } from 'rxjs/operators';

const interval$ = interval(1000).pipe(
  tap((x: any) => console.log('interval', x)),
  take(5)
);

// NOTE: must click 3 times for this observable to complete
const click$ = fromEvent(document, 'click').pipe(
  tap(x => console.log('clicked', x)),
  take(3)
);

/** forkJoin WON'T emit until all observables have *completed* */
forkJoin(interval$, click$).subscribe(
  // will not log here UNTIL 3 clicks and 5 seconds on interval
  ([val1, val2]) => console.log('forkJoin result:', val1, val2),
  err => console.log(err),
  () => console.log('forkJoin complete')
);

// takes object too.
forkJoin({ interval: interval$, 'click pos': click$ }).subscribe(
  // will not log here UNTIL 3 clicks and 5 seconds on interval
  result => console.log('forkJoin result2:', result),
  err => console.log(err),
  () => console.log('forkJoin complete2')
);
