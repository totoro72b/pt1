import { interval } from "rxjs";
import { mapTo, scan, filter, tap, takeWhile, startWith } from "rxjs/operators";

// lab 2 - count down timer
const counter$ = interval(500);
const obs1$ = counter$.pipe(
  mapTo(-1),
  scan((acc, val) => acc + val, 10),
  tap({
    next: (x: any) => console.log("tap", x),
    complete: () => console.log("complete"),
    error: (x: any) => console.log("error", x)
  }), // tap shows us the observable keeps emitting negative values and doesn't complete
  filter(x => x >= 0)
);
obs1$.subscribe(val => console.log(val));

const START_VALUE = 10;

// lab 2 - count down timer fix
const obs2$ = counter$.pipe(
  mapTo(-1),
  scan((acc, val) => acc + val, START_VALUE), // started with 10 and immediately -1, so first shown val =9
  startWith("asdf"), // to fix starting on 9, we tag on 10
  tap(x => console.log("obs2 stream", x)),
  takeWhile(x => x >= 0)
);
obs2$.subscribe({
  next: val => console.log(val),
  complete: () => console.log("obs2 complete!")
});
