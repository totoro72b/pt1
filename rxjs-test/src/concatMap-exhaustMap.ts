import { concatMap, take, delay, mergeMap, exhaustMap } from 'rxjs/operators';
import { fromEvent, interval, of } from 'rxjs';

const click$ = fromEvent(document, 'click');

// concatMap preserves the order of client-side execution
const fakeRequest$ = (value: number) =>
  of(value).pipe(delay(Math.floor(Math.random() * 1000)));
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
// click$
//   .pipe(concatMap(() => interval(1000)))
//   .subscribe(x => console.log('click interval value', x));

// scenario: this is the login request and we want to ignore subsequent requests while the first one is being resolve:
// like a spammy user clicks really fast
// soln: use exhaustMap! clicking really fast 3 times will only have the first one thru

click$
  .pipe(
    exhaustMap(() => {
      i += 1;
      console.log('send request for exhaustMap', i); // exhaustMap won't get here if it currently has an active inner subscription
      return fakeRequest$(i);
    })
  )
  .subscribe(x => console.log('exhaustMap got value', x));
