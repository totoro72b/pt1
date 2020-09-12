import { fromEvent, of } from "rxjs";
import {
  concatMap,
  delay,
  exhaustMap,
  map,
  mergeMap,
  share,
  switchMap,
  tap
} from "rxjs/operators";

/**
 * scenario: a spammy user like ayo clicks really fast
 * we want to use exhaustMap to only register the first click and send a request and ignore
 * the subsequent clicks.
 *
 * following also shows the difference between concatMap, mergeMap, exhaustMap and switchMap
 */

console.clear();
let i = 0;
const click$ = fromEvent(document, "click").pipe(
  tap(() => {
    i += 1; // inc counter upon each click
  }),
  map(() => i),
  share() // so counter is incremented once per click regardless of number of subscribers
);

// concatMap preserves the order of client-side execution
const fakeRequest$ = (x: number) =>
  of(x).pipe(
    delay(500 + Math.floor(Math.random() * 1000)),
    map(x => "Request Response:" + x)
  );

/** concatMap will emit responses in the order of they were sent */
click$
  .pipe(
    concatMap(x => {
      return fakeRequest$(x);
    })
  )
  .subscribe(x => console.log("concatMap result:", x));

/** mergeMap will not emit responses in the order of they were sent;
 * quick responses will show up first
 */
click$
  .pipe(
    mergeMap(x => {
      return fakeRequest$(x);
    })
  )
  .subscribe(x => console.log("mergeMap result:", x));

/** exhaustMap ignores newer clicks while waiting for a response for the current request */
click$
  .pipe(
    exhaustMap(x => {
      return fakeRequest$(x);
    })
  )
  .subscribe(x => console.log("exhaustMap result:", x));

/** switchMap *cancels* the previous request (if it hasn't been resolved) and switch to waiting for the response of the new request */
click$
  .pipe(
    switchMap(x => {
      return fakeRequest$(x);
    })
  )
  .subscribe(x => console.log("switchMap result:", x));
