import {from} from 'rxjs/observable/from';
import {tap, map} from 'rxjs/operators';

// do also known as tap in pipable operators
const src = from([1,2,3,4,5]);
src.pipe(
  tap(x=>console.log('before map', x)),
  map(x=>x*x),
  tap(x=>console.log('after map', x)),
).subscribe(x=>console.log('final result', x));
