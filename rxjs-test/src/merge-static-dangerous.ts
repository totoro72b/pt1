import { interval, merge, of } from 'rxjs';
import { tap } from 'rxjs/operators';

const source1$ = of('hello', 'world', 'asdf');
const source2$ = interval(500).pipe(tap(x => console.log('from source 2', x)));
const source3$ = interval(1000).pipe(tap(x => console.log('from source 3', x)));

/** merge does NOT limit number of ACTIVE inner observables
 * so everybody talks whenever they want
 */
merge(source2$, source1$, source3$).subscribe(x =>
  console.log('MERGE got ', x)
);
