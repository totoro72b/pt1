// Only emit when the current value is different than the last.
import {from} from 'rxjs/observable/from';
import {distinctUntilChanged} from 'rxjs/operators';

const src = from([1,1,2,2,2,3,4,5,4,3,2]);
src.pipe(
  distinctUntilChanged()
).subscribe(
  x=>console.log(x)
);

//obj reference must mach
const obj1 = {a:1};
const obj2 = {a:1}; //considered distinct
const src2 = from([obj1, obj2]);
src2.pipe(
  distinctUntilChanged()
).subscribe(
  x=>console.log('obj', x)
);
