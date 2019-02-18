import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DetailCardComponent } from './detail-card/detail-card.component';
import { ReactiveFormsModule } from '@angular/forms';
import { NewEditModalComponent } from './new-edit-modal/new-edit-modal.component';
import { NgbModalModule, NgbModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [AppComponent, DetailCardComponent, NewEditModalComponent],
  entryComponents: [NewEditModalComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    NgbModule.forRoot() // enable usage for modal, dropdown, all nbg stuff
    // NgbModalModule // must import here in order to use
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
