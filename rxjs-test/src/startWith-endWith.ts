import { of } from 'rxjs';
import { endWith, startWith } from 'rxjs/operators';

const numbers$ = of(1, 2, 3);
/** append and prepend values to stream */
numbers$
  .pipe(
    endWith('d', 'e', 'f'),
    startWith('a', 'b', 'c')
  )
  .subscribe(console.log);
