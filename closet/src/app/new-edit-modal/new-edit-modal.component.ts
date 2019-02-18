import { Component, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Item } from '../types';

@Component({
  selector: 'app-new-edit-modal',
  templateUrl: './new-edit-modal.component.html',
  styleUrls: ['./new-edit-modal.component.scss']
})
export class NewEditModalComponent implements OnInit {
  constructor(public activeModal: NgbActiveModal) {}
  // modal input
  item: Item = null;
  allCategories: string[];
  selectedCategory: string = null;

  ngOnInit() {
    // assign input data
    const data = this.item;
    console.log('input data', data);
  }

  get titleText(): string {
    if (this.item) {
      return 'Edit Item';
    }
    return 'Add Item';
  }

  get btnText(): string {
    if (this.item) {
      return 'Save';
    }
    return 'Add';
  }

  setCategory(cat: string) {
    this.selectedCategory = cat;
  }

  btnClickHandler(): void {
    // TODO
    console.log('save data... exit');
    this.activeModal.close('Close click');
  }
}
