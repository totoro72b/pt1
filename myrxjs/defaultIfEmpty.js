// Emit given value if nothing is emitted before completion.
//
import { defaultIfEmpty } from 'rxjs/operators';
import { of } from 'rxjs/observable/of';
import { empty } from 'rxjs/observable/empty';

const src = of();
src.pipe(
  defaultIfEmpty('default value')
).subscribe(
  x=>console.log(x)
);

const src2 = of(1,2,3);
src2.pipe(
  defaultIfEmpty('default value')
).subscribe(
  x=>console.log('src2', x)
);

const src3 = empty();
src3.pipe(
  defaultIfEmpty('default value')
).subscribe(
  x=>console.log('src3', x)
);
