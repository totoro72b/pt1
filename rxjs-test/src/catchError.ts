// catchError!

console.clear();

// begin lesson code
import { fromEvent, empty, of, throwError } from 'rxjs';
import { ajax } from 'rxjs/ajax';
import {
  debounceTime,
  pluck,
  distinctUntilChanged,
  switchMap,
  catchError,
  delay,
  tap
} from 'rxjs/operators';

const BASE_URL = 'https://api.openbrewerydb.org/breweries';

// streams
const click$ = fromEvent(document, 'click');
const fakeRequest$ = (value: any) => of(value.slice(0, 2)).pipe(delay(300));

click$
  .pipe(
    debounceTime(200),
    tap(() => console.log('clicked')),
    switchMap(() =>
      // we are catching the error on the ajax observable returned by switchMap
      // if catchError is put on the click$ stream, it'll complete that stream upon error
      // which we don't want (wont' accept further input values)
      fakeRequest$([123]).pipe(
        catchError((error, caught) => {
          console.log('error', error);
          //   return caught;  // returning caught will retry
          return empty();
        })
      )
    )
  )
  .subscribe((response: any) => {
    console.log('got response!', response);
  });
