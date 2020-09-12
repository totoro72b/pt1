import { fromEvent, of, timer } from "rxjs";
import {
  delay,
  exhaustMap,
  filter,
  finalize,
  map,
  pluck,
  switchMap,
  takeUntil,
  tap
} from "rxjs/operators";

/** This lab demostrates the usage of exhaustMap, switchMap, takeUntil and finalize
 *
 * scenario: press "a" on the keyboard to kick start a long running observable
 * which sends a fake request repeatedly at a regular interval (to simulate pooling a resource)
 *
 * - exhaustMap: while the long running observable is active,
 * press "a" will *not* kick start another long running observable due to exhaustMap.
 *
 * - switchMap: switch & map each emission from "timer" to a fakeRequest$ observable, AND
 * cancelling a previous fakeRequest$ observable when upon a new timer emission
 * NOTE: fakeRequest$ has a longer delay sometimes, and these requests are cancelled by switchMap
 *
 * - takeUntil: completes the current observable upon an emission from $stop
 *
 * - finalize: being called when current observable completes (or errs)
 */

console.log('press "a" to start and "s" to stop');
const start$ = fromEvent(document, "keydown").pipe(
  pluck("code"),
  filter(x => x === "KeyA")
);
const stop$ = fromEvent(document, "keydown").pipe(
  pluck("code"),
  filter(x => x === "KeyS")
);

const fakeRequest$ = (x: any) =>
  of(x).pipe(
    delay(x % 2 === 0 ? 500 : 1500), // NOTE: longer delays on odd values!
    map(x => "got fake data:" + x)
  );

const obs = start$.pipe(
  // one request per sec
  tap(x => console.log("start key pressed")),
  /** exhaustMap: ignores all other "start" signals during the current active long-running observable */
  exhaustMap(() => {
    console.log("about to start long running observable");
    /** timer emits once per second */
    return timer(0, 1000).pipe(
      tap(x => console.log("timer emits", x)),
      switchMap(x => fakeRequest$(x)),
      takeUntil(stop$),
      finalize(() => {
        console.log("finalized");
      })
    );
  })
);

obs.subscribe((x: any) => console.log("request result:", x));
