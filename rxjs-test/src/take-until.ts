import { fromEvent, of, interval } from "rxjs";
import { tap, takeUntil } from "rxjs/operators";

// takeUntil completes based on the emission of another observable
const source$ = interval(500);
const click$ = fromEvent(document, "click");

const obs$ = source$.pipe(
  tap(x => console.log("tap", x)),
  takeUntil(click$)
);

obs$.subscribe({
  next: console.log,
  complete: () => "complete!"
});
