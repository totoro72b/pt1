import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewEditModalComponent } from './new-edit-modal.component';

describe('NewEditModalComponent', () => {
  let component: NewEditModalComponent;
  let fixture: ComponentFixture<NewEditModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewEditModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewEditModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
