import { fromEvent, interval } from 'rxjs';
import { mergeMap, switchMap } from 'rxjs/operators';

const click$ = fromEvent(document, 'click');

// mergeMap is dangerous.
// everytime i click, mergeMap subscribes to a *new * inner observable
// no limit to the number of active inner subscriptions by default
click$
  .pipe(mergeMap(() => interval(1000)))
  .subscribe(x => console.log('mergeMap', x));

// a safer default choice of flattening operator: swithcMap
click$
  .pipe(switchMap(() => interval(1000)))
  .subscribe(x => console.log('switchmap', x));

// example of cancelling inner observables on mouseup
// const interval$ = interval(1000);
// const mouseup$ = fromEvent(document, "mouseup");
// const mousedown$ = fromEvent(document, "mousedown");
// mousedown$
//   .pipe(
//     mergeMap(() =>
//       interval$.pipe(
//         tap(x => console.log("tap ", x)),
//         takeUntil(mouseup$)
//       )
//     )
//   )
//   .subscribe(console.log);
