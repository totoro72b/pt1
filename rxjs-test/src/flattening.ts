import { fromEvent, interval } from 'rxjs';
import { mergeMap, map, takeUntil, tap, switchMap } from 'rxjs/operators';
import { ajax } from 'rxjs/ajax';

const interval$ = interval(1000);
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

// example of using mergeMap to send http requests
// const coordinates$ = click$.pipe(
//   map((event: any) => ({ x: event.clientX, y: event.clientY }))
// );
// const coordinatesWithSave$ = coordinates$.pipe(
//   mergeMap(coords => {
//     const obs = ajax.post("https://www.mocky.io/v2/5185415ba171ea3a00704eed");
//     return obs; // mergeMap subscribes to this inner observable and emit its values
//   })
// );
// coordinatesWithSave$.subscribe(console.log);
