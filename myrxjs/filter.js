import {filter} from 'rxjs/operators';
import {from} from 'rxjs/observable/from';

const src = from([1,2,3,4,5]);
src.pipe(
  filter(x => x % 2 === 0)
).subscribe(
  x=>console.log(`even val ${x}`)
);
