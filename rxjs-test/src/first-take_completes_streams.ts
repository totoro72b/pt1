import { of, interval } from "rxjs";
import {
  filter,
  mapTo,
  scan,
  tap,
  first,
  take,
  takeWhile
} from "rxjs/operators";

// take completes the observable after the specified number of takes
const source$ = of(1, 2, 3, 4, 5);

// take 3 and completes
const obs1$ = source$.pipe(take(3));
obs1$.subscribe({
  next: console.log,
  complete: () => console.log("take complete!")
});
// note that take completes obs1$, but doesn't prevent source$
// from emitting further values. check out below

// first == filter + take(1)
const obs2$ = source$.pipe(first(x => x > 3));
obs2$.subscribe({
  next: console.log,
  complete: () => console.log("first complete!")
});
