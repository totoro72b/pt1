import {startWith} from 'rxjs/operators';
import {of} from 'rxjs/observable/of';

const src = of(1,2,3);
src.pipe(
  startWith(-10, -9, 0)
).subscribe(
  x=> console.log(x)
);
