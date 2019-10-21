import { timer, of, fromEvent, interval } from 'rxjs';
import {
  tap,
  filter,
  pluck,
  delay,
  exhaustMap,
  takeUntil,
  switchMapTo,
  finalize
} from 'rxjs/operators';

// pull random id application
const start$ = fromEvent(document, 'keydown').pipe(
  pluck('code'),
  filter(x => x === 'KeyA')
);

const stop$ = fromEvent(document, 'keydown').pipe(
  pluck('code'),
  filter(x => x === 'KeyS')
);

let i = 0;
const fakeRequest$ = (x: any) => of(x).pipe(delay(500));

// idea: start kicks off sending requests at an interval, and stop stops it
const obs = start$.pipe(
  // one request per sec
  tap(x => console.log('start key')),
  exhaustMap(() => {
    i += 1;
    console.log('about to start long running observable', i);
    // click starts this long running observable, until it's completed by the stop key
    // meanwhile all other clicks are ignored by exhaustmap
    return timer(0, 1000).pipe(
      // timer starts at 0 and repeats once / sec
      switchMapTo(fakeRequest$(i)),
      takeUntil(stop$),
      finalize(() => {
        console.log('finalized');
      })
    );
  })
);

obs.subscribe((x: any) => console.log('sub result got ', x));
