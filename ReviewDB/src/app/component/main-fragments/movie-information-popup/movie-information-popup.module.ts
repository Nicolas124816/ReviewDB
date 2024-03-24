import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { MovieInformationPopupComponent } from './movie-information-popup.component';
import { StarIconModule } from '../../field-components/icons/star-icon/star-icon.module'

@NgModule({
  imports: [
    CommonModule,
    StarIconModule
  ],
  declarations: [
    MovieInformationPopupComponent,
  ],
  exports: [
    MovieInformationPopupComponent,
  ],
})
export class MovieInformationPopupModule { }
