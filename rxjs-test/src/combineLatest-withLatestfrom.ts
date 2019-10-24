import { fromEvent, combineLatest, interval } from "rxjs";
import { mapTo, map, withLatestFrom } from "rxjs/operators";

// combineLatest. will not emit until all observables have emitted something
const obs1$ = fromEvent(document, "click").pipe(mapTo("click"));
const obs2$ = fromEvent(document, "keyup").pipe(mapTo("key up!"));

combineLatest(obs1$, obs2$)
  .pipe(map(([val1, val2]) => `${val1} - ${val2}`))
  .subscribe(console.log);

// withLatestFrom augments a primary observable with other stuff
obs1$
  .pipe(
    // note: similar to combineLatest, will not emit until primary and augmented obs have emitted
    // this interval is managed internally
    withLatestFrom(interval(1000))
  )
  .subscribe(x => console.log(`clicked at ${x} seconds`));
