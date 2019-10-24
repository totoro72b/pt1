import { fromEvent, interval, merge, empty } from "rxjs";
import {
  filter,
  pluck,
  tap,
  mapTo,
  switchMap,
  scan,
  takeUntil,
  takeWhile,
  startWith
} from "rxjs/operators";

// merge  - a static creation operator
const start$ = fromEvent(document, "keyup").pipe(
  pluck("code"),
  filter(x => x === "KeyS"),
  mapTo(true)
);
const pause$ = fromEvent(document, "keyup").pipe(
  pluck("code"),
  filter(x => x === "KeyQ"),
  mapTo(false)
);

const counter$ = interval(1000);
const INITIAL_VAL = 10;

const fancyCounter$ = merge(start$, pause$).pipe(
  switchMap(toStart => {
    console.log("to start?", toStart);
    if (toStart) {
      return counter$;
    } else {
      return empty(); // empty obs don't emit nothing
    }
  }),
  mapTo(-1),
  // scan emits every value before the observable completes
  // apparently scan keeps track of the accumulator state during pause and re-start
  scan((acc, cur) => {
    console.log("scan acc", acc, "cur", cur);
    return acc + cur;
  }, INITIAL_VAL),
  startWith(INITIAL_VAL), // this value emits w/o start$ or pause$ emits anything!
  takeWhile(x => x >= 0) // once negative, completes fancyCounter$ subscription
);

fancyCounter$.subscribe(
  x => console.log("fancy counter val", x),
  err => console.log(err),
  () => console.log("complete fancy counter")
);
