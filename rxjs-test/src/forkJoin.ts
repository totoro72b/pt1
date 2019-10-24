import { interval, fromEvent, forkJoin } from "rxjs";
import { tap, take } from "rxjs/operators";

const interval$ = interval(1000).pipe(
  tap((x: any) => console.log("interval", x)),
  take(5)
);
const click$ = fromEvent(document, "click").pipe(
  tap(x => console.log("clicked", x)),
  take(3)
);

// WON'T emit until all observables have *completed*
forkJoin(interval$, click$).subscribe(
  // will not log here UNTIL 3 clicks and 5 seconds on interval
  ([val1, val2]) => console.log("got stuff", val1, val2),
  err => console.log(err),
  () => console.log("complete")
);

// takes object too.
forkJoin({ interval: interval$, "click pos": click$ }).subscribe(
  // will not log here UNTIL 3 clicks and 5 seconds on interval
  result => console.log("got stuff2", result),
  err => console.log(err),
  () => console.log("complete")
);
