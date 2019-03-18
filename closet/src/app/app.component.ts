import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Item } from './types';
import { flatMap, debounceTime, distinctUntilChanged } from 'rxjs/operators';
import { NgbModal, NgbModalOptions } from '@ng-bootstrap/ng-bootstrap';
import { NewEditModalComponent } from './new-edit-modal/new-edit-modal.component';

const ALL = 'all';
const ngbModalOptions: NgbModalOptions = {
  backdrop: 'static',
  keyboard: false,
  size: 'lg'
};

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'closet';
  items: Item[] = null;
  filteredItems: Item[] = [];
  allCategories: string[] = [];
  searchfg: FormGroup = new FormGroup({
    search: new FormControl(),
    category: new FormControl()
  });

  constructor(private modal: NgbModal) {}

  get selectedCategory(): string {
    return this.searchfg.get('category').value;
  }

  openModal(itemIdx: number): void {
    console.log('openmodal idx', itemIdx);
    // item = null in new mode
    // item = instance in edit mode
    const modalRef = this.modal.open(NewEditModalComponent, ngbModalOptions);
    modalRef.componentInstance.item =
      itemIdx !== null ? this.items[itemIdx] : null;
    modalRef.componentInstance.itemIndex = itemIdx;
    modalRef.componentInstance.allCategories = this.allCategories;
  }

  filterItems(changes: any) {
    const keyword = changes.search || '';
    const category = changes.category === ALL ? '' : changes.category;
    console.log('category is', category);
    console.log('change str', keyword);
    // TODO add debounce
    this.filteredItems = this.items.filter(
      x =>
        x.description.toLowerCase().includes(keyword.toLowerCase()) &&
        x.category.toLowerCase().includes(category)
    );
  }

  setCategory(cat: string): void {
    this.searchfg.get('category').setValue(cat);
  }

  ngOnInit() {
    this.searchfg.get('category').setValue(ALL);
    this.searchfg.valueChanges
      .pipe(
        debounceTime(300),
        distinctUntilChanged() // FIXME: doesn't really work
      )
      .subscribe(changes => {
        this.filterItems(changes);
      });
    this.items = [
      {
        category: 'top',
        description: 'fav blouse',
        imgUrl:
          'https://images.anthropologie.com/is/image/Anthropologie/4110084326168_089_b?$an-category$&qlt=80&fit=constrain',
        id: 1
      },
      {
        category: 'bottom',
        description: 'skirt',
        imgUrl:
          'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7z09tXLDZODUEJLM5q6neP0NXLBhjckrZz6ZIXOzjBsLCP9NVrw',
        id: 2
      },
      {
        category: 'accessory',
        description: 'pink hat',
        imgUrl:
          'https://www.acnestudios.com/on/demandware.static/-/Sites-acne-product-catalog/default/dwdfbd534d/images/D4/D40001-/1500x/D40001-418_C.jpg',
        id: 3
      }
    ];
    this.allCategories = this.items.map(x => x.category.toLowerCase());
    this.allCategories.push(ALL);
    this.filteredItems = [...this.items];
  }
}
