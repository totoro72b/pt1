/** observable creations */
// VV all the creation operators!!
import { interval, timer, fromEvent, of, range, from } from "rxjs";

const observer = {
  next: (val: any) => console.log("val", val),
  err: (val: any) => console.log("err", val),
  complete: () => console.log("complete!")
};

// 1) observable creation from dom events
const source$ = fromEvent(document, "keyup");
const sub1 = source$.subscribe(observer);
const sub2 = source$.subscribe(observer);

// after 3 seconds, sub1 no longer prints but sub2 continues to pickup keyup events
setTimeout(() => {
  console.log("unsubing");
  sub1.unsubscribe();
}, 3000);

// 2) observable creation using of
const source2$ = of([1, 7], 2, 3, 4, 5); // of does not flatten inner stuff
console.log("before of");
source2$.subscribe(observer); // emits synchronously! (blocks until complete)
console.log("after of");

// 3) observable creation using range
const source3$ = range(15, 5);
console.log("before range");
source3$.subscribe(observer); // emits synchronously! (blocks until complete)
console.log("after range");

// 4) observable creation using from
//**from is like a more intelligent of; it flattens inner crap */
const source4$ = from([1, 2, 3, [4, 5]]); // it flattens 1 level => 1,2,3 [4,5]
console.log("before from");
source4$.subscribe(observer); // emits synchronously! (blocks until complete)
console.log("after from");

// from an iterator
function* iter() {
  yield "hello";
  yield "world";
}

const source5$ = from(iter()); // it flattens to 'hello', 'world'
source5$.subscribe(observer);

const source6$ = from("asdf"); // it flattens to a, s, d, f
source6$.subscribe(observer);

// 5) observable creation using interval
// interval emits numbers in sequence at the time interval that you specified
const source7$ = interval(1000);
source7$.subscribe(observer); // waits for 1s before emitting the first element

// 6) observable creation using timer
// timer emits numbers in sequence at an initial time (dueTime), then subsequently at the specified interval
const source8$ = timer(0, 2000); // emits right away, then every 2 s
// const source8$ = timer(0); // emits right away, then done!
source8$.subscribe(observer);
