import { from } from 'rxjs/observable/from';
import { first } from 'rxjs/operators';

const source = from([1, 2, 3, 4, 5]);
source.pipe(
  first() // just get first val
).subscribe(
  { next: x=>console.log(x),
    complete:  ()=>console.log('complete')
  }
);

const src = from([1, 2, 3, 4, 5]);
src.pipe(
  first(x=> x === 3) // first value that pass predicate
).subscribe(
  x=>console.log('first to pass', x),
);
