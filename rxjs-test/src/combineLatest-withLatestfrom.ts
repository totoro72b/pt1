import { combineLatest, fromEvent, interval } from 'rxjs';
import { map, mapTo, withLatestFrom } from 'rxjs/operators';

console.log('need to BOTH click AND press a key to see something!');

const obs1$ = fromEvent(document, 'click').pipe(mapTo('click'));
const obs2$ = fromEvent(document, 'keyup').pipe(mapTo('key up!'));

/** combineLatest. will not emit until ALL observables have emitted something */
const clickAndPress$ = combineLatest(obs1$, obs2$).pipe(
  map(([val1, val2]) => `${val1} - ${val2}`)
);

clickAndPress$.subscribe(x => console.log('combineLatest result:', x));

/** withLatestFrom augments a primary observable with other stuff
 *  similar to combineLatest, will not emit until primary and augmented obs have emitted,
 * then emit whenever primary observable emits
 */
clickAndPress$
  .pipe(
    // this interval is managed internally
    withLatestFrom(interval(1000)) // NOTE: if you click right away, won't see log until 1s has passed
  )
  .subscribe(x =>
    console.log(`withLatestFrom: clicked or keyup at ${x} seconds`)
  );
