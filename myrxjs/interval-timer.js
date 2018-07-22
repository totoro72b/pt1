import {interval} from 'rxjs/observable/interval';
import {timer} from 'rxjs/observable/timer';

// emit a number in sequence at a fixed interval (starting from 0)
const src = interval(1000); //every 1 sec
src.subscribe(x=>console.log('interval subscriber1', x));

src.subscribe(x=>console.log('interval subscriber2', x));

// emit a value once when timer goes off
const src2 = timer(3000);
src2.subscribe({
  //x=>console.log('timer', x),
  next: (x)=>console.log('timer next', x),
  complete: (x)=>console.log('timer complete', x)
});
//
// emit a value after 2s, then every .5 sec
const src3 = timer(2000, 500);
src3.subscribe({
  next: (x)=>console.log('timer 2 next', x),
  complete: (x)=>console.log('timer 2 complete', x)
});
