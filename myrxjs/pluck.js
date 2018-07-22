import { from } from 'rxjs/observable/from';
import { pluck } from 'rxjs/operators';

const src = from([{ name: 'Joe', age: 30 }, { name: 'Sarah', age: 35 }]);
src.pipe(
  pluck('name')
).subscribe(x=>console.log(x));
