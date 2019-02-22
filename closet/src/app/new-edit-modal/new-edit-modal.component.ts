import { Component, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Item } from '../types';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-new-edit-modal',
  templateUrl: './new-edit-modal.component.html',
  styleUrls: ['./new-edit-modal.component.scss']
})
export class NewEditModalComponent implements OnInit {
  constructor(public activeModal: NgbActiveModal) {}
  // modal input
  input: any = {};
  editMode = false;
  // item: Item = null;
  // selectedCategory: string = null;
  allCategories: string[];

  itemFG: FormGroup = new FormGroup({
    description: new FormControl(),
    name: new FormControl(),
    category: new FormControl(),
    imgUrl: new FormControl()
  });

  ngOnInit() {
    // assign input data
    const data: Item = this.input.item;
    if (this.input.item) {
      // assign values to form group
      const item: Item = this.input.item;
      this.itemFG.get('description').setValue(item.description);
      this.itemFG.get('category').setValue(item.category);
      this.itemFG.get('imgUrl').setValue(item.imgUrl);
      this.editMode = true;
    }
  }

  get titleText(): string {
    if (this.editMode) {
      return 'Edit Item';
    }
    return 'Add Item';
  }

  get btnText(): string {
    if (this.editMode) {
      return 'Save';
    }
    return 'Add';
  }

  get selectedCategory(): string {
    return this.itemFG.value['category'];
  }

  setCategory(cat: string) {
    this.itemFG.get('category').setValue(cat);
  }

  btnClickHandler(): void {
    // TODO
    console.log('form group', this.itemFG.value);
    // this.activeModal.close('Close click');
  }
}
