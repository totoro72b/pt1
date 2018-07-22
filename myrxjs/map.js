import {from } from 'rxjs/observable/from';
import {map} from 'rxjs/operators';

const src = from([1,2,3,4]).pipe(
  map(x=>x*x)
);

src.subscribe(x=>console.log(x));
