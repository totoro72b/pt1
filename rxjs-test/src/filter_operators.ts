import { of, fromEvent } from "rxjs";
import { pluck, filter } from "rxjs/operators";

/**filter operators */
of(1, 2, 3, 4, 5)
  .pipe(filter(val => val > 2))
  .subscribe(console.log);

const keyup$ = fromEvent(document, "keyup");
const keycode$ = keyup$.pipe(pluck("code"));
keycode$.subscribe(console.log);

const enter$ = keycode$.pipe(filter(code => code === "Enter"));
enter$.subscribe((x: any) => console.log(typeof x, x));
