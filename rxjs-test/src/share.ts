import { of, combineLatest, forkJoin, interval } from "rxjs";
import {
  delay,
  map,
  filter,
  tap,
  switchMap,
  take,
  concatMap,
  share
} from "rxjs/operators";

// share to avoid doing the same computation twice
const a$ = interval(500).pipe(take(4));
const b$ = interval(600).pipe(take(2));
const c$ = interval(700).pipe(take(2));

function calculateStuff(a: number, b: number, c: number) {
  console.log("calculating", a, b, c);
  return a + b + c;
}

const fakeRequest$ = (x: any) =>
  of(x).pipe(
    delay(100),
    map(x => `Saved OK: ${x}`)
  );

const numbers$ = combineLatest(a$, b$, c$).pipe(
  tap(x => console.log("source on", x)),
  filter(([a, b, c]) => a > 1),
  map(([a, b, c]) => calculateStuff(a, b, c)),
  share() // avoid calling everything else up to this point upon each subscription
);

numbers$.subscribe(x => console.log("show in UI", x));

// imitate network requests
numbers$
  .pipe(
    tap(x => console.log("gonna send request on", x)),
    // switchMap will drop some logs if new values come too fast,
    //since it drops all previous active inner observables upon any new emission from source
    // switchMap(x => fakeRequest$(x))
    concatMap(x => fakeRequest$(x))
  )
  .subscribe((x: any) => console.log("Saving results", x));
