import { Observable, Subscriber } from "rxjs";
const observer = {
  next: (x: any) => console.log("observer next val:", x),
  error: (err: any) => console.log("observer err val:", err),
  complete: () => console.log("observer complete!")
};

// observable with an interval emit thing that can be cancelled
// upon subscriber.complete when you return the func to clearInterval
const obs2 = new Observable(subscriber => {
  let count = 0;
  const id = setInterval(() => {
    subscriber.next(count);
    console.log("setInterval id is", id); // id stays the same
    // NOTE: calling subscriber.complete() triggers the execution of the returned clearInterval func below
    subscriber.complete();
    count += 1;
  }, 500);

  // called upon subscriber complete.
  // w/o clearInterval, the interval keeps emitting even after subscriber.complete() is called
  return () => {
    console.log("return func called (upon subscriber complete)");
    clearInterval(id);
  };
});

obs2.subscribe(observer);
