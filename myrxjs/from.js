import {from} from 'rxjs/observable/from';

// takes Observabe, promise, array or iterable
from([1,3,4,5]).subscribe(x => console.log(x));
