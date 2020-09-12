import { asyncScheduler, fromEvent } from "rxjs";
import {
  auditTime,
  debounceTime,
  filter,
  pluck,
  sample,
  sampleTime,
  tap,
  throttleTime
} from "rxjs/operators";

const source$ = fromEvent(document, "click");

source$.pipe(debounceTime(1000)).subscribe(x => console.log("debounceTime", x));

/** debounce using interval: version 2 */
// source$
//   .pipe(debounce(() => interval(1000)))
//   .subscribe(x => console.log("debounce version", x));

source$
  .pipe(throttleTime(1000))
  .subscribe(x => console.log("throttleTime leading", x));

source$
  .pipe(throttleTime(1000, asyncScheduler, { trailing: true, leading: false }))
  .subscribe(x => console.log("throttleTime trailing", x));

source$.pipe(auditTime(1000)).subscribe(x => console.log("auditTime ", x)); // same as trailing trottleTime

// NOTE: for the same source and trottle time, for every leading there's a trailing
source$.pipe(sampleTime(1000)).subscribe(x => console.log("sampleTime ", x));

const notifier$ = fromEvent(document, "keyup").pipe(
  pluck("code"),
  tap(x => console.log("keyup", x)),
  filter(x => x === "Enter")
);
// emits the last value in the window defined by the notifier emissions
source$.pipe(sample(notifier$)).subscribe(x => console.log("sample", x));
