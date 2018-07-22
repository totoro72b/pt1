import {mapTo} from 'rxjs/operators';
import {interval} from 'rxjs/observable/interval';

const src = interval(800);
src.pipe(
  mapTo('hello') //mapTo takes a CONSTANT value.
).subscribe(
  x=>console.log(x)
);
