import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Item } from '../types';

@Component({
  selector: 'app-detail-card',
  templateUrl: './detail-card.component.html',
  styleUrls: ['./detail-card.component.scss']
})
export class DetailCardComponent implements OnInit {
  @Input() item: Item;
  @Input() index: number;
  @Output() editEmitter = new EventEmitter<number>();
  constructor() {}

  ngOnInit() {}
  editClickHandler(idx: number) {
    console.log('click index', idx);
    this.editEmitter.emit(idx);
  }
}
