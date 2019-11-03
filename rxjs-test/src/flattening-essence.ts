import { fromEvent } from 'rxjs';
import { ajax } from 'rxjs/ajax';
import { map, mergeMap } from 'rxjs/operators';

console.log('click to see!');

const click$ = fromEvent(document, 'click');

/** map vs mergeMap
 * example of using mergeMap to send http requests
 */

// when observable emits regular values, map does the trick
const coordinates$ = click$.pipe(
  map((event: any) => ({ x: event.clientX, y: event.clientY }))
);

// but when an observable emits an observable, map sucks
const coordinatesWithSaveUsingMap$ = coordinates$.pipe(
  map(coords => {
    const obs = ajax.post('https://www.mocky.io/v2/5185415ba171ea3a00704eed');
    return obs; // ahhh observable!
  })
);
coordinatesWithSaveUsingMap$.subscribe(x => console.log('map result:', x));

/** mergeMap subscribes to the inner observable and emit its values */
const coordinatesWithSave$ = coordinates$.pipe(
  mergeMap(coords => {
    const obs = ajax.post('https://www.mocky.io/v2/5185415ba171ea3a00704eed');
    return obs; // mergeMap subscribes to this inner observable and emit its values
  })
);
coordinatesWithSave$.subscribe(x => console.log('mergeMap result:', x));
