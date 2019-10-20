import { interval } from "rxjs";
import { mapTo, scan, filter, tap, takeWhile } from "rxjs/operators";

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

// lab 2 - count down timer fix
const obs2$ = counter$.pipe(
  mapTo(-1),
  scan((acc, val) => acc + val, 10),
  tap({
    next: (x: any) => console.log("tap with take while", x),
    complete: () => console.log("complete-take while"),
    error: (x: any) => console.log("error", x)
  }), // tap shows us the observable stops emitting after encountering first -1
  takeWhile(x => x >= 0)
);
obs2$.subscribe(val => console.log(val));
