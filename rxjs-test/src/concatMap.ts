import { concatMap, take, delay, mergeMap } from 'rxjs/operators';
import { fromEvent, interval, of } from 'rxjs';

const click$ = fromEvent(document, 'click');

const fakeRequest$ = (value: number) =>
  of(value).pipe(delay(Math.floor(Math.random() * 1000)));

// concatMap preserves the order of client-side execution
let i = 0;
click$
  .pipe(
    concatMap(() => {
      // using concatMap results will show up in order
      // mergeMap(() => { // results will show up out of order
      i += 1;
      console.log('send request', i);
      return fakeRequest$(i);
    })
  )
  .subscribe(x => console.log('got value', x));

// NOTE: further clicks will not ever be executed because the first active inner observable
// never finishes
click$
  .pipe(concatMap(() => interval(1000)))
  .subscribe(x => console.log('click interval value', x));
