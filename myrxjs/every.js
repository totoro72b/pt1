import {every} from 'rxjs/operators';
import {filter} from 'rxjs/operators';
import {tap} from 'rxjs/operators';
import { of } from 'rxjs/observable/of';
import { interval } from 'rxjs/observable/interval';

//emit 5 values
const source = of(1, 2, 3, 4, 5);
// every returns true iff every element passes predicate when complete
source.pipe(
  every(x=> x%2 === 0)
).subscribe(x=>console.log(x)); //false, cuz not every element is even

const evenSrc = of(2, 4, 6);
// every returns true iff every element passes predicate when complete
evenSrc.pipe(
  every(x=> x%2 === 0)
).subscribe(
  {
    next: x=>console.log('even src:', x), //true
    complete: ()=>console.log('even src complete')
  }
);

// never finishes?
const fullInterval = interval(500);
fullInterval.pipe(
  every(x=>x%2===0)
).subscribe(x=>console.log('fullInt', x)); //false, cuz not every element is even

const evenInterval= interval(500);
evenInterval.pipe(
  tap(x=>console.log('tap before', x)),
  filter(x=>x%2===0),
  tap(x=>console.log('tap after', x)),
  every(x=>x%2===0),
).subscribe(x=>console.log('evenInt', x)); // this NEVER returns cuz it never reaches complete and always passes predicate!
