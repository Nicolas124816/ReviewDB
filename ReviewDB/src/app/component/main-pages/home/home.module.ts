import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HomeComponent } from './home.component';
import { MovieScoreFieldModule } from '../../../component/field-components/movie-score-field/movie-score-field.module'
import { ForKidsIconModule } from '../../../component/field-components/icons/for-kids-icon/for-kids-icon.module'
import { MovieInformationPopupModule } from '../../main-fragments/movie-information-popup/movie-information-popup.module'
import { StarIconModule } from '../../field-components/icons/star-icon/star-icon.module'

@NgModule({
  declarations: [
    HomeComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    ForKidsIconModule,
    MovieScoreFieldModule,
    MovieInformationPopupModule,
    StarIconModule
  ],
  exports: [
    HomeComponent,
  ],
})
export class HomeModule { }
