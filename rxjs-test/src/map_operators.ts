/** map operators */
console.clear();

import { of, fromEvent } from "rxjs";
import { map, pluck, mapTo } from "rxjs/operators";

of(1, 2, 3)
  .pipe(map(value => value * 10))
  .subscribe(console.log);

const keyup$ = fromEvent(document, "keyup");
const keycode$ = keyup$.pipe(map((event: any) => event.code));
keycode$.subscribe(console.log);

// pluck a property
const keycodeWithPluck$ = keyup$.pipe(pluck("code")); // can be nested too
keycodeWithPluck$.subscribe(console.log);

const pressed$ = keyup$.pipe(mapTo("keyup!"));
pressed$.subscribe(console.log);
