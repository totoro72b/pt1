import { Component, OnInit, Input } from '@angular/core';
import { Item } from '../types';

@Component({
  selector: 'app-detail-card',
  templateUrl: './detail-card.component.html',
  styleUrls: ['./detail-card.component.scss']
})
export class DetailCardComponent implements OnInit {

  @Input() item: Item;
  constructor() { }

  ngOnInit() {
  }

}
