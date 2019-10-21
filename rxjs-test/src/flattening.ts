import { fromEvent, interval } from "rxjs";
import { mergeMap, map, takeUntil, tap } from "rxjs/operators";
import { ajax } from "rxjs/ajax";

const interval$ = interval(1000);
const click$ = fromEvent(document, "click");

click$
  .pipe(
    // everytime i click, mergeMap subscribes to a *new * inner observable
    // no limit to the number of activ einner subscriptions by default
    mergeMap(() => interval(1000))
  )
  .subscribe(console.log);

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
